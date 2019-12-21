import random
import string
import json
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from utils.qq_login import QQOauth
from utils.mp_login import MPOauth
from utils.wb_login import WBOauth
from .serializers import CodeSerializer, UserRegSerializer, UserDetailSerializer, OAuthSerializer
from utils.sendcode import Msg, Mail
from .models import VerifyCode

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None):
        try:
            # 用户名和手机都能登录
            user = User.objects.get(Q(username=username) | Q(mobile=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SMSCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
    发送验证码
    """
    serializer_class = CodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']
        email = serializer.validated_data['email']
        # 生成四位数字验证码
        code = ''.join(random.sample(string.digits, 6))
        if email:
            mail = Mail()
            try:
                mail.send(email, code)
                code_record = VerifyCode(code=code, email=email)
                code_record.save()  # 保存到数据库
                return Response({'msg': '发送成功'})
            except Exception as e:
                return Response({'msg': '发送失败'})
        if mobile:
            msg = Msg()
            sms_status = msg.send(mobile, code)
            if sms_status['return_code'] != '00000':  # 服务商提供的发送成功的状态码
                return Response({'msg': '发送失败'})
            else:
                code_record = VerifyCode(code=code, mobile=mobile)
                code_record.save()  # 保存到数据库
                return Response({'msg': '发送成功'})


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    create:
    创建用户
    retrieve:
    用户详情
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer
        return UserDetailSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticated()]
        elif self.action == 'creat':
            return []
        return []

    # 返回自己的信息
    def get_object(self):
        return self.request.user


class OauthBindViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    绑定用户
    """
    queryset = User.objects.all()
    serializer_class = OAuthSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        headers = self.get_success_headers(serializer.data)
        return Response({'token': token}, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class QqLogin(APIView):
    """
    获取用户信息
    """

    def get(self, request):
        qq = QQOauth()
        code = request.query_params.get('code')
        access_token = qq.get_access_token(code)
        openid = qq.get_openid(access_token)
        userinfo = qq.get_userinfo(access_token, openid)
        try:
            user = User.objects.get(openid=openid)
            user.last_login = datetime.now()
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({
                'user': UserDetailSerializer(user, context={'request': request}).data,
                'token': token,
                'code': '1'
            })
        except:
            return Response({'userinfo': json.loads(userinfo), 'code': '0', 'openid': openid})


class MpLogin(APIView):
    """
    获取用户信息
    """

    def get(self, request):
        mp = MPOauth()
        code = request.query_params.get('code')
        openid = mp.get_openid(code)
        try:
            user = User.objects.get(openid=openid)
            user.last_login = datetime.now()
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({
                'token': token,
                'flag': '1'
            })
        except:
            return Response({
                'flag': '0',
                'openid': openid
            })


class WbLogin(APIView):
    """
    获取用户信息
    """

    def get(self, request):
        weibo = WBOauth()
        code = request.query_params.get('code')
        res = weibo.get_access_token(code)
        res_dict = json.loads(res)
        access_token = res_dict['access_token']
        uid = res_dict['uid']
        userinfo = weibo.get_user_info(access_token, uid)
        try:
            user = User.objects.get(openid=uid)
            user.last_login = datetime.now()
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({
                'user': UserDetailSerializer(user, context={'request': request}).data,
                'token': token,
                'code': '1'
            })
        except:
            return Response({'userinfo': json.loads(userinfo), 'code': '0', 'openid': uid})


def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和user信息
    """
    user.last_login = datetime.now()
    user.save()
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data
    }
