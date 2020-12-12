from rest_framework import serializers, validators

from .models import Category, Genre, Title
from .validators import year_validator


class CustomField(serializers.SlugRelatedField):
    def to_representation(self, instance):
        return {'name': instance.name, 'slug': instance.slug}


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        required=False,
        validators=[
            validators.UniqueValidator(queryset=Category.objects.all())
        ],
    )

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        required=False,
        validators=[validators.UniqueValidator(queryset=Genre.objects.all())],
    )

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(required=False, read_only=True)
    genre = CustomField(
        many=True,
        required=False,
        slug_field='slug',
        queryset=Genre.objects.all(),
    )
    category = CustomField(
        required=False, slug_field='slug', queryset=Category.objects.all()
    )
    year = serializers.IntegerField(
        required=False, validators=[year_validator]
    )

    class Meta:
        fields = '__all__'
        model = Title
