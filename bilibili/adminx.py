import xadmin
from .models import Videolist, UserInfo


class VideoListAdmin(object):
    list_display = ['title', 'pubtime', 'play', 'danmaku', "like_count", 'favorite', 'reply']


class UserInfoAdmin(object):
    list_display = ['follows', 'fans', 'likes', 'plays', "add_time", ]


xadmin.site.register(Videolist, VideoListAdmin)
xadmin.site.register(UserInfo, UserInfoAdmin)
