import xadmin
from .models import Comment


class CommentAdmin(object):
    list_display = ['pid', 'user', 'add_time']


xadmin.site.register(Comment, CommentAdmin)
