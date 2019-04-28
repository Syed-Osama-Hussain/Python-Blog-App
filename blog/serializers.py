from rest_framework import serializers
from .models import Post


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    date_posted = serializers.DateTimeField()
    author = UserSerializer(read_only=True)
