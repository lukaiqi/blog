from rest_framework import mixins, viewsets, filters
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Article, ArticleType
from .serializers import ArticleSerializer, ArticleTypeSerializer, ArticleDetailSerializer, CommentAddSerializer
from .filters import CommentFilter


class ArticleTypeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ArticleType.objects.all()
    serializer_class = ArticleTypeSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    list:
    显示文章列表
    creat:
    新建文章
    update:
    更新
    retrieve:
    显示文章详情
    """
    queryset = Article.objects.all().order_by('-id')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 过滤，搜索，排序
    search_fields = ('title', 'content')  # 搜索
    ordering_fields = ('add_time',)  # 排序

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ArticleDetailSerializer
        elif self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleSerializer


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    新建评论
    """

    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter
    serializer_class = CommentAddSerializer
