from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Client
from .serializers import ClientSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


class ClientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    访客信息列表
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination
