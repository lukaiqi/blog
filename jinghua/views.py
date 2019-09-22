from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets, filters
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
    queryset = Jinghua.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 过滤，搜索，排序
    # filter_class = ArticleFilter  # django-filter自定义过滤
    search_fields = ('title', 'content')  # 搜索
    ordering_fields = ('add_time',)  # 排序
