from rest_framework import serializers
from .models import Danmu, Jinyan


class DanmuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Danmu
        fields = '__all__'


class JinyanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jinyan
        fields = '__all__'


class CountSerializer(serializers.ModelSerializer):
    count = serializers.CharField(max_length=10)
    date = serializers.CharField(max_length=10)

    class Meta:
        model = Danmu
        fields = ('count', 'date')
