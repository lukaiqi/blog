from rest_framework import mixins, viewsets, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentListSerializer, CommentAddSerializer
from .filters import CommentFilter


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 15
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
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination  # 分页
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 过滤，搜索，排序
    search_fields = ('title', 'content')  # 搜索
    ordering_fields = ('add_time',)  # 排序


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
    显示评论列表
    creat:
    新建评论
    """

    queryset = Comment.objects.all().order_by('-add_time')
    pagination_class = StandardResultsSetPagination  # 分页
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentAddSerializer
        elif self.action == 'list':
            return CommentListSerializer

        return CommentListSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'list':
            return []
        return []
