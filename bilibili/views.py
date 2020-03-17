import time

from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Videolist, UserInfo
from .serializers import VideoListSerializer, UserInfoSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 15
    # page_query_param = 'p' #页码名称
    page_size_query_param = 'page_size'
    max_page_size = 100


class VideoListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    哔哩哔哩投稿视频列表
    """

    # 获取查询日期，默认返回当前日期数据
    def get_queryset(self):
        try:
            date = self.request.query_params['date']
        except:
            date = time.strftime('%Y-%m-%d')
        return Videolist.objects.filter(add_time=date).order_by('-pubtime')

    # 认证方式
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = VideoListSerializer
    pagination_class = StandardResultsSetPagination


class UserInfoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    哔哩哔哩播放信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination
