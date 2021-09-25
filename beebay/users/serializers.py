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

#trying to limit the user from seeing userdetails that are not their own
    # def validate(self, data):
    #check that the user id is the logged in user
    #     print('DATA',data)
        # user = CustomUser.objects.get(id=data['customuser_id'])
        # id = user.id
        # current_user = self.context['request'].user
        # if id == current_user:
        #     raise serializers.ValidationError("NOPE")
        # return data

# new code for updating user details - name,email    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email',instance.email)
        # instance.password = validated_data.get('password',instance.password)
        instance.save()
        return instance