from collections import OrderedDict

import requests
import re

from django.utils.deprecation import MiddlewareMixin
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Client
from .serializers import ClientSerializer


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


class ClientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    访客信息列表
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('-id')
    pagination_class = StandardResultsSetPagination


class ClientIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 获取客户端IP
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        # 获取请求头
        user_agent = request.META['HTTP_USER_AGENT']
        # 判断是否有useragent
        if user_agent:
            ua = user_agent
        else:
            ua = '空'
        # 获取访问路径
        path = request.path_info
        # 通过ip定位
        try:
            client = Client()
            res = requests.get('http://ip.yqie.com/ip.aspx?ip={}'.format(ip))
            addr = re.search('id="AddressInfo".*value="(.*?)".*?', res.text)
            client.ip = ip
            client.addr = addr.group(1)
            client.path = path
            client.user_agent = ua
            client.save()
        except:
            pass

        return None
