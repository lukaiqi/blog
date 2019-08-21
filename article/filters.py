from django_filters.rest_framework import filters, FilterSet

from .models import Article


class ArticleFilter(FilterSet):
    type_name = filters.NumberFilter(method='article_type_filter')

    def article_type_filter(self, queryset, name, value):
        # return queryset.filter(type_name_id=value)
        return queryset.filter(type_name=value)

    class Meta:
        model = Article
        fields = ['type_name']
