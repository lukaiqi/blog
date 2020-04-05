import json
from django.utils.deprecation import MiddlewareMixin
from client.models import Client
import requests


class ClientIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        user = request.user
        # admin登录后台，不记录
        if user.is_superuser:
            pass
        else:
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
                res = requests.get('http://ipquery.market.alicloudapi.com/query?ip={}'.format(ip),
                                   headers={"Authorization": "APPCODE 6b5974d1336f415ca1901fd6ef6fe95b"})
                res_json = res.json()
                ret = res_json['ret']
                data = res_json['data']
                if ret == 200:
                    country = data['country']
                    city = data['city']
                    area = data['area']
                    isp = data['isp']
                    client = Client()
                    client.ip = ip
                    client.country = country
                    client.city = city
                    client.area = area
                    client.path = path
                    client.isp = isp
                    client.user_agent = ua
                    client.save()
            except Exception as e:
                pass
        return None
