import xadmin
from article.models import Article, ArticleType, Comment


class ArticleAdmin(object):
    list_display = ['title', 'type_name', 'click_num', 'add_time']


class ArticletypeAdmin(object):
    list_display = ['id', 'name']


class CommentAdmin(object):
    list_display = ['pid', 'user', 'add_time']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleType, ArticletypeAdmin)
xadmin.site.register(Comment, CommentAdmin)
