from rest_framework import serializers
from .models import Article, ArticleType, Comment


class ArticleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleType
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    """
    文章列表序列化
    """

    class Meta:
        model = Article
        fields = '__all__'

    def get_type(self, obj):
        return obj.type.name


class ArticleCreateSerialize(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    """
    创建文章
    """

    class Meta:
        model = Article
        fields = '__all__'


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
        return obj.user.nickname


class ArticleDetailSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    comments = CommentListSerializer(many=True)
    """
    文章列表序列化
    """

    class Meta:
        model = Article
        fields = '__all__'

    def get_type(self, obj):
        return obj.type.name
