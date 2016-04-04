from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserExtension
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)
    last_login = serializers.CharField(max_length=255)
    is_superuser = serializers.BooleanField(default=False)
    first_name = serializers.CharField(max_length=255, allow_blank=True)
    last_name = serializers.CharField(max_length=255, allow_blank=True)
    email = serializers.EmailField(max_length=255)
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    date_joined = serializers.DateTimeField(default=timezone.now())
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User

    def create(self, validated_data):
        if self.is_superuser:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password')
        instance.last_login= validated_data.get('last_login')
        instance.is_superuser= validated_data.get('is_superuser')
        instance.firstname= validated_data.get('first_name')
        instance.last_name= validated_data.get('last_name')
        instance.email= validated_data.get('email')
        instance.is_staff= validated_data.get('is_staff')
        instance.is_active= validated_data.get('is_active')
        instance.date_joined= validated_data.get('date_joined')
        instance.username= validated_data.get('username')
        instance.save()
        return instance


class UserExtSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    birthday = serializers.DateField(default=timezone.now())
    number = serializers.IntegerField()

    class Meta:
        model = UserExtension

    def create(self, validated_data):
        return UserExtension.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user')
        instance.birthday = validated_data.get('birthday')
        instance.number = validated_data.get('number')
        instance.save()

        return instance
