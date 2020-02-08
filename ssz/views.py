from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import BiliBiliInfo,BiliBiliVideoList, QQMusic
from .serializers import BiliBiliSerializer, QQMusicSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 15
    # page_query_param = 'p' #页码名称
    page_size_query_param = 'page_size'
    max_page_size = 100


class BiliViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    哔哩哔哩投稿视频列表
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = BiliBiliSerializer
    queryset = BiliBiliVideoList.objects.all()
    pagination_class = StandardResultsSetPagination


class QmViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    qq音乐歌曲列表
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = QQMusicSerializer
    queryset = QQMusic.objects.all()
    pagination_class = StandardResultsSetPagination
