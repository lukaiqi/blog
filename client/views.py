import requests
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    访客信息列表
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('-id')


class GetInfo(APIView):
    """
    获取请求IP
    """

    def get(self, request):
        info = {}
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        try:
            res = requests.get('http://ipquery.market.alicloudapi.com/query?ip={}'.format(ip),
                               headers={"Authorization": "APPCODE 6b5974d1336f415ca1901fd6ef6fe95b"})
            res_json = res.json()
            ret = res_json['ret']
            data = res_json['data']
            if ret == 200:
                info['addr'] = data['country'] + data['city'] + data['area'] + data['isp']
                info['loc'] = data['lng'] + ',' + data['lat']
            else:
                info['addr'] = '未知'
        except Exception as e:
            info['addr'] = '未知'
        try:
            res = requests.get(
                'https://free-api.heweather.net/s6/weather/now?location={}&key=51a39d27a18248fd8179ae76f49b8ca1'.format(
                    info['loc']))
            res_json = res.json()
            now = res_json['HeWeather6'][0]['now']
            info['weather'] = now
        except:
            pass
        return Response(info)
