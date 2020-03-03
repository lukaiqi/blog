import xadmin
from .models import Client


class ClientAdmin(object):
    list_display = ['ip', 'add_time', 'path', 'addr', 'isp_name']


xadmin.site.register(Client, ClientAdmin)
