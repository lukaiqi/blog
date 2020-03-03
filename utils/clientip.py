from django.utils.deprecation import MiddlewareMixin
from client.models import Client

visit_ip = ''


class ClientIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 获取访问者IP
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        # 获取访问路径
        path = request.path_info
        client = Client()
        client.ip = ip
        client.path = path
        client.save()
        return None
