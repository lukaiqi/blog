from django_filters.rest_framework import filters, FilterSet

from .models import Article, Comment


class ArticleFilter(FilterSet):
    type_name = filters.NumberFilter(method='article_type_filter')

    def article_type_filter(self, queryset, name, value):
        return queryset.filter(type_name=value)

    class Meta:
        model = Article
        fields = ['type_name']


class CommentFilter(FilterSet):
    pid = filters.NumberFilter(method='comment_filter')

    def comment_filter(self, queryset, name, value):
        return queryset.filter(pid=value)

    class Meta:
        model = Comment
        fields = ['pid']
