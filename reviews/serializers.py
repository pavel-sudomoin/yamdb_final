from rest_framework import serializers
from .models import Review, Comment, Title
from django.utils.translation import gettext_lazy as _


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        extra_kwargs = {'score': {'min_value': 1, 'max_value': 10}}

    def create(self, validated_data):
        if Review.objects.filter(
            author=validated_data.get('author'),
            title=validated_data.get('title'),
        ).exists():
            raise serializers.ValidationError(
                _('Only one review allowed per title')
            )
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
