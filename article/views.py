from future.backports import OrderedDict
from rest_framework import mixins, viewsets, filters, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Article, ArticleType
from .serializers import ArticleSerializer, ArticleCreateSerialize, ArticleTypeSerializer, ArticleDetailSerializer, \
    CommentAddSerializer
from .filters import CommentFilter


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('current', self.page.number),
            ('size', self.page.paginator.per_page),
            ('results', data)
        ]))


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
    pagination_class = StandardResultsSetPagination
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get_serializer_class(self):

        if self.action == 'list':
            return ArticleSerializer
        elif self.action == 'create':
            return ArticleCreateSerialize
        elif self.action == 'retrieve':
            return ArticleDetailSerializer
        return ArticleSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminUser()]
        elif self.action == 'put':
            return [IsAdminUser()]

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'code': 0, 'body': '', 'msg': '操作成功'}, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'code': 0, 'body': '', 'msg': '操作成功'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'code': 0, 'body': '', 'msg': '操作成功'}, status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    新建评论
    """

    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentFilter
    serializer_class = CommentAddSerializer
