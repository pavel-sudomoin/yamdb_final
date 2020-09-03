import uuid
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='category_name', unique=True
    )
    slug = models.SlugField(
        max_length=50, verbose_name='category_slug', unique=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Category, self).save(*args, **kwargs)
        self.full_clean()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='genre_name', unique=True
    )
    slug = models.SlugField(
        max_length=50, verbose_name='genre_slug', unique=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Genre, self).save(*args, **kwargs)
        self.full_clean()

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name='title_name')
    year = models.IntegerField(
        verbose_name='title_year', blank=True, null=True
    )
    description = models.CharField(
        max_length=200, verbose_name='title_description', blank=True, null=True
    )
    genre = models.ManyToManyField(
        Genre, related_name='titles', verbose_name='title_genre', blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='title_category',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
        ordering = ['pk']
