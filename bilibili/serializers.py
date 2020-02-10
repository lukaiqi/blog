from rest_framework import serializers
from .models import Videolist, UserInfo


class VideoListSerializer(serializers.ModelSerializer):
    """
    用户详情
    """

    class Meta:
        model = Videolist
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    """
    用户详情
    """

    class Meta:
        model = UserInfo
        fields = '__all__'
