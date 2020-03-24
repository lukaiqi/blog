import xadmin
from .models import Client


class ClientAdmin(object):
    list_display = ['ip', 'country', 'city', 'area', 'isp', 'user_agent', 'path', 'add_time']


xadmin.site.register(Client, ClientAdmin)
