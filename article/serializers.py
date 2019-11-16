from rest_framework import serializers
from .models import Article, ArticleType, Comment


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


class CommentAddSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    """
    添加评论
    """

    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    """
    评论列表
    """

    class Meta:
        model = Comment
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username
