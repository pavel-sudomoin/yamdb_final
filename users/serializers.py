from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )


class UserSerializerForUsers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )
        read_only_fields = ('role',)


class UserCreateByEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class UserCreateTokenSerializer(UserCreateByEmailSerializer):
    confirmation_code = serializers.UUIDField(required=True)
