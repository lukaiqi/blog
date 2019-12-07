import xadmin
from .models import Jinghua


class JinGhuaAdmin(object):
    list_display = ['nickname', 'otime', 'status']


xadmin.site.register(Jinghua, JinGhuaAdmin)
