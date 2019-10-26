from rest_framework import serializers
from .models import Jinghua


class JinghuaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jinghua
        fields = '__all__'


class CountSerializer(serializers.ModelSerializer):
    count = serializers.CharField(max_length=10)
    date = serializers.CharField(max_length=10)

    class Meta:
        model = Jinghua
        fields = ('count', 'date')
