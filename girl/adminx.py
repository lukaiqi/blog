import xadmin
from .models import Music, Sentence


class MusicAdmin(object):
    list_display = ['name', 'url', "add_time"]


class SentenceAdmin(object):
    list_display = ['content', "add_time"]


xadmin.site.register(Music, MusicAdmin)
xadmin.site.register(Sentence, SentenceAdmin)
