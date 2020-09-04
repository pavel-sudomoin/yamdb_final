import uuid
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='Category name', unique=True
    )
    slug = models.SlugField(
        max_length=50, verbose_name='Category slug', unique=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Category, self).save(*args, **kwargs)
        self.full_clean()


class Genre(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='Genre name', unique=True
    )
    slug = models.SlugField(
        max_length=50, verbose_name='Genre slug', unique=True
    )

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Genre, self).save(*args, **kwargs)
        self.full_clean()


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name='Title name')
    year = models.IntegerField(
        verbose_name='Title year', blank=True, null=True
    )
    description = models.CharField(
        max_length=200, verbose_name='Title description', blank=True, null=True
    )
    genre = models.ManyToManyField(
        Genre, related_name='titles', verbose_name='Title genre', blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Title category',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
        ordering = ('pk',)

    def __str__(self):
        return self.name
