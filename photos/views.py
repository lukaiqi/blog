from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from photos.models import Photo
from photos.serializers import PhotoListSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PhotoListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Photo.objects.all().order_by('-id')
    serializer_class = PhotoListSerializer
    pagination_class = StandardResultsSetPagination
