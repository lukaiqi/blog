import xadmin
from .models import Danmu, Jinyan


class DanmuAdmin(object):
    list_display = ['nickname', 'content', 'sendtime']


class JinyanAdmin(object):
    list_display = ['dnic', 'snic', 'endtime', 'otype']


xadmin.site.register(Danmu, DanmuAdmin)
xadmin.site.register(Jinyan, JinyanAdmin)
