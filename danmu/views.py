from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import DanmuSerializer, JinyanSerializer
from .models import Danmu, Jinyan


class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 10
    # page_query_param = 'p' #页码名称
    page_size_query_param = 'page_size'
    max_page_size = 100


class DanmuViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DanmuSerializer
    pagination_class = StandardResultsSetPagination  # 分页

    def get_queryset(self):
        searchtype = self.request.query_params.get('serachtype')
        keyword = self.request.query_params.get('keyword')
        print(searchtype, keyword)
        if searchtype == '1':
            # 昵称精确查找弹幕
            res = Danmu.objects.filter(nickname=keyword).order_by('id')
            return res
        elif searchtype == '2':
            #     弹幕搜索
            res = Danmu.objects.filter(content__contains=keyword).order_by('id')
            return res


class JinyanViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Jinyan.objects.all().order_by('id')
    serializer_class = JinyanSerializer
    pagination_class = StandardResultsSetPagination  # 分页

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        searchtype = self.request.query_params.get('searchtype')
        if searchtype == '1':
            # 查被禁言的发言记录
            res = Jinyan.objects.filter(dnic=keyword).order_by('id')
            return res
        elif searchtype == '2':
            # 查房管禁言了哪些用户
            res = Jinyan.objects.filter(snic=keyword).order_by('id')
            return res
        else:
            return Jinyan.objects.all().order_by('id')
