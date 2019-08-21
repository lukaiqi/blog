from rest_framework import serializers
from .models import Article, ArticleType


class ArticleSerializer(serializers.ModelSerializer):
    type_name = serializers.SerializerMethodField()
    """
    文章列表序列化
    """

    class Meta:
        model = Article
        fields = '__all__'

    def get_type_name(self, obj):
        return obj.type_name.name
