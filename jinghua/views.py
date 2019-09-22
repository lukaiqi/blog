from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Jinghua
from .serializers import DakaListSerializer


# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DakaListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DakaListSerializer
    queryset = Jinghua.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)  # 过滤，搜索，排序
    search_fields = ('nickname',)  # 搜索
