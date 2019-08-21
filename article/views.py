from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from .filters import ArticleFilter


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 10
    # page_query_param = 'p' #页码名称
    page_size_query_param = 'page_size'
    max_page_size = 100


class ArticleListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
    list:
    显示文章列表
    creat:
    新建文章
    retrieve:
    显示文章详情
    """
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination  # 分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 过滤，搜索，排序
    # filter_class = ArticleFilter  # django-filter自定义过滤
    search_fields = ('title', 'content')  # 搜索
    ordering_fields = ('add_time',)  # 排序

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



