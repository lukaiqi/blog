import random
import string
import json
from collections import OrderedDict
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from utils.qq_login import QQOauth
from utils.wb_login import WBOauth
from .serializers import CodeSerializer, UserRegSerializer, UserDetailSerializer, OAuthSerializer, UserSerializer
from utils.sendcode import Mail
from .models import VerifyCode

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None):
        try:
            # 用户名和手机都能登录
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class CodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
    发送验证码
    """
    serializer_class = CodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        # 生成四位数字验证码
        code = ''.join(random.sample(string.digits, 6))
        mail = Mail()
        try:
            mail.send(email, code)
            code_record = VerifyCode(code=code, email=email)
            code_record.save()  # 保存到数据库
            return Response({'msg': '发送成功'})
        except:
            return Response({'msg': '发送失败'})


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('current', self.page.number),
            ('size', self.page.paginator.per_page),
            ('results', data)
        ]))


class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    list:
    获取用户列表
    create:
    创建用户
    retrieve:
    用户详情
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer
        return UserDetailSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
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


class QQLogin(APIView):
    """
    获取QQ用户信息
    """

    def get(self, request):
        qq = QQOauth()
        code = request.query_params.get('code')
        # 没有code参数
        if code is None:
            return Response({'msg': '非法请求'})
        access_token = qq.get_access_token(code)
        # 获取acces_Token失败
        if access_token is None:
            return Response({'msg': 'code非法'})
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


class WbLogin(APIView):
    """
    获取微博用户信息
    """

    def get(self, request):
        weibo = WBOauth()
        code = request.query_params.get('code')
        # 没有code参数
        if code is None:
            return Response({'msg': '非法请求'})
        res = weibo.get_access_token(code)
        res_dict = json.loads(res)
        try:
            access_token = res_dict['access_token']
            uid = res_dict['uid']
        except:
            return Response({'msg': 'code非法'})
        userinfo = weibo.get_userinfo(access_token, uid)
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
