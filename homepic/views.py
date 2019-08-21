import random
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .serializers import HomepicSerializer, HomepicAddSerializer
from .models import Homepic
from utils.danmu import Danmu


class HomePicViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        count = Homepic.objects.count()
        i = random.randint(1, count)
        return Homepic.objects.filter(id=i)

    def get_serializer_class(self):
        if self.action == 'list':
            return HomepicSerializer
        elif self.action == 'create':
            return HomepicAddSerializer
        return HomepicSerializer

    def get_permissions(self):
        if self.action == 'list':
            return []
        elif self.action == 'create':
            return [IsAuthenticated()]
        return []


class DanmuView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        global res
        dm = Danmu()
        keyword = request.query_params.get('nn')
        searchtype = request.query_params.get('type')
        if searchtype == '1':
            # 昵称精确匹配
            res = dm.matchnn(keyword)
            # return Response(res)
        elif searchtype == '2':
            # 昵称搜索
            res = dm.searchnn(keyword)
            # return Response(res)
        elif searchtype == '3':
            # 弹幕搜索
            res = dm.searchtxt(keyword)
            # return Response(res)
        else:
            pass
        return Response(res)