from rest_framework import serializers
from posts.models import Post
from accounts.models import User, OtpModel


class OtpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpModel
        fields = [
            'pre_code',
            'mobile_phone'
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'area_code',
            'mobile_phone',
            'password'
        ]

        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions',
            'id'
        ]

        extra_kwargs = {
            'last_login': {'read_only': True},
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = [
            'id',
            'create_at',
            'update_at',
            'is_published',
            'en_slug',
            'fa_slug'
        ]


class RetrievePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = [
            'id',
            'en_slug',
            'fa_slug',

        ]
