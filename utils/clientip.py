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
        # 获取请求头
        user_agent = request.META['HTTP_USER_AGENT']
        # 判断是否有useragent
        if user_agent:
            if 'Android' in user_agent:
                plantform = 'Android'
            elif 'iPhone' in user_agent:
                plantform = 'iPhone '
            elif 'Mac' in user_agent:
                plantform = 'Mac'
            elif 'Windows' in user_agent:
                plantform = 'Windows'
            elif 'okhttp' in user_agent:
                plantform = 'Android'
            else:
                plantform = 'other'
        else:
            plantform = 'None'
        # 通过ip定位
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
            }
            res = requests.get('https://ipchaxun.com/{}/'.format(ip), headers=headers)
            # 解析返回的网页
            html = BeautifulSoup(res.text, 'lxml')
            # 提取数据
            results = html.select('.info label .value')
            addr = results[1].text
            isp_name = results[2].text

        except Exception as e:
            addr = '获取失败'
            isp_name = '获取失败'
        # 获取访问路径
        path = request.path_info
        if 'xadmin' or 'ckeditor' in path:
            pass
        else:
            client = Client()
            client.ip = ip
            client.path = path
            client.addr = addr
            client.isp_name = isp_name
            client.plantform = plantform
            client.save()
        return None
