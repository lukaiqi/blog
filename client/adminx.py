import xadmin
from .models import Client


class ClientAdmin(object):
    list_display = ['ip', 'addr', 'user_agent', 'path', 'visit_time']


xadmin.site.register(Client, ClientAdmin)
