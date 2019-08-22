from rest_framework import serializers
from .models import Homepic


class HomepicSerializer(serializers.ModelSerializer):
    """
    图片列表序列化
    """

    class Meta:
        model = Homepic
        fields = '__all__'


class HomepicAddSerializer(serializers.ModelSerializer):
    """
    图片列表序列化
    """

    class Meta:
        model = Homepic
        fields = ('url',)

