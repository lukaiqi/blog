import xadmin
from .models import Client


class ClientAdmin(object):
    list_display = ['ip', 'path', 'addr', 'isp_name', 'plantform', 'add_time']


xadmin.site.register(Client, ClientAdmin)
