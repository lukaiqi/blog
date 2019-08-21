import xadmin
from users.models import VerifyCode, UserAvatar


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


class UserAvatarAdmin(object):
    list_display = ['id', 'avatar', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(UserAvatar, UserAvatarAdmin)
