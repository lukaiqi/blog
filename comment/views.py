from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Comment
from .serializers import CommentListSerializer, CommentAddSerializer
from .filters import CommentFilter


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 10
    # page_query_param = 'p' #页码名称
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    显示评论列表
    creat:
    新建评论
    """

    queryset = Comment.objects.all().order_by('-add_time')

    # serializer_class = CommentSerializer
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
