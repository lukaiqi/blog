import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Jinghua
from .serializers import JinghuaListSerializer, CountSerializer


# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义分页属性
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DakaListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # 认证方式
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 权限
    permission_classes = (IsAuthenticated,)
    queryset = Jinghua.objects.all().order_by('-id')
    serializer_class = JinghuaListSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)  # 过滤，搜索，排序
    search_fields = ('nickname',)  # 搜索


class JHCountViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CountSerializer

    def get_queryset(self):
        today = datetime.date.today()
        list = []
        for i in range(30):
            date = today - datetime.timedelta(days=i)
            lastdate = today - datetime.timedelta(days=i + 1)
            num_temp = Jinghua.objects.filter(otime__range=(lastdate, date)).count()
            list.append({'count': num_temp, 'date': lastdate.strftime('%Y-%m-%d')})
        return list
