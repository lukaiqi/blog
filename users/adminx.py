import xadmin
from users.models import VerifyCode


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'email', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
