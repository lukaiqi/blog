import re
from datetime import datetime, timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from .models import VerifyCode

User = get_user_model()


class CodeSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    # 函数名必须：validate + 验证字段名
    def validate_mobile(self, mobile):
        """
        验证手机号
        :param mobile:
        :return:
        """
        # 验证手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('手机号已被注册')
        # 验证手机号码格式
        if not re.match('^1[3456789]\d{9}$', mobile):
            raise serializers.ValidationError('手机号非法')
        one_min_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_min_ago, mobile=mobile):
            raise serializers.ValidationError('距离上次发送未超过60s')
        return mobile


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情
    """

    class Meta:
        model = User
        fields = ('username', 'nickname', 'gender', 'email', 'mobile', 'avatar')


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户注册
    """
    code = serializers.CharField(required=True, max_length=6, min_length=6, write_only=True,
                                 label='验证码',
                                 error_messages={
                                     'blank': '请输入验证码',
                                     'required': '请输入验证码',
                                     'max_length': '验证码格式错误',
                                     'min_length': '验证码格式错误'
                                 }, help_text='验证码')
    # 验证用户名是否存在
    username = serializers.CharField(required=True, allow_blank=False, label='用户名',
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户已存在')])
    # 密码,write_only表示只写，不返回
    password = serializers.CharField(style={'input_type': 'password'}, label='密码', write_only=True)

    # 设置密码
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by('-add_time')
        five_min_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
        if verify_records:
            last_record = verify_records[0]
            if five_min_ago > last_record.add_time:
                raise serializers.ValidationError('验证码过期')
            if last_record.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('username', 'code', 'mobile', 'password')


class OAuthSerializer(serializers.ModelSerializer):
    openid = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    # 密码,write_only表示只写，不返回
    password = serializers.CharField(style={'input_type': 'password'}, label='密码', write_only=True)

    def create(self, validated_data):
        user = super(OAuthSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        attrs['nickname'] = attrs['username']
        return attrs

    class Meta:
        model = User
        fields = ('username', 'password', 'openid')
