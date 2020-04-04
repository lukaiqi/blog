from django_filters import filters, FilterSet

from .models import Article, Comment


class CommentFilter(FilterSet):
    pid = filters.NumberFilter(field_name='pid')

    class Meta:
        model = Comment
        fields = ['pid']
