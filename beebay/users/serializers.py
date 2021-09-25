from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


# new code for updating user details - name,email    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        # instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance