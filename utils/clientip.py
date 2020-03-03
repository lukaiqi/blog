from django.utils.deprecation import MiddlewareMixin
from client.models import Client
import requests
from bs4 import BeautifulSoup


class ClientIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 获取访问者IP
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        # 通过ip定位
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
            }
            res = requests.get('http://ip138.com/iplookup.asp?ip={}&action=2'.format(ip), headers=headers)
            # 解析返回的网页
            html = BeautifulSoup(res.content.decode('gb2312'), 'lxml')
            # 提取数据
            li = html.select('.ul1 li')[0].text
            addr = li.split('：')[1]
        except Exception as e:
            addr = '获取失败'
        # 获取访问路径
        path = request.path_info
        if 'xadmin' not in path:
            client = Client()
            client.ip = ip
            client.path = path
            client.addr = addr
            client.save()
        return None
