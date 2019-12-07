from django_filters.rest_framework import filters, FilterSet

from .models import Article, Comment


class CommentFilter(FilterSet):
    pid = filters.NumberFilter(method='comment_filter')

    def comment_filter(self, queryset, name, value):
        return queryset.filter(pid=value)

    class Meta:
        model = Comment
        fields = ['pid']
