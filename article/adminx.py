import xadmin
from article.models import Article, ArticleType


class ArticleAdmin(object):
    list_display = ['title', 'type_name', 'click_num']


class ArticletypeAdmin(object):
    list_display = ['id', 'name']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleType, ArticletypeAdmin)
