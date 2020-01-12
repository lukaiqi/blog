from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Bilibili, QQMusic
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
    传感器的值
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = BiliBiliSerializer
    queryset = Bilibili.objects.all()
    pagination_class = StandardResultsSetPagination


class QmViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    传感器的值
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = QQMusicSerializer
    queryset = QQMusic.objects.all()
    pagination_class = StandardResultsSetPagination
