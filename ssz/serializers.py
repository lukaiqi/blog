from rest_framework import serializers
from .models import Bilibili, QQMusic


class BiliBiliSerializer(serializers.ModelSerializer):
    """
    用户详情
    """

    class Meta:
        model = Bilibili
        fields = '__all__'


class QQMusicSerializer(serializers.ModelSerializer):
    """
    用户详情
    """

    class Meta:
        model = QQMusic
        fields = '__all__'
