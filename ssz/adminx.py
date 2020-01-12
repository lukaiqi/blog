import xadmin
from .models import Bilibili, QQMusic


class BilibiliAdmin(object):
    list_display = ['title', 'pubtime', 'play', 'danmaku', "likes", 'favorite', 'reply']


class QQMusicAdmin(object):
    list_display = ['title', 'comments', 'pubdate']


xadmin.site.register(QQMusic, QQMusicAdmin)
xadmin.site.register(Bilibili, BilibiliAdmin)
