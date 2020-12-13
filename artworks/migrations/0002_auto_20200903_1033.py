# Generated by Django 3.0.5 on 2020-09-03 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('artworks', '0001_initial')]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={
                'ordering': ['id'],
                'verbose_name': 'Title',
                'verbose_name_plural': 'Titles',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(
                max_length=200, unique=True, verbose_name='category_name'
            ),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='category_slug'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(
                max_length=200, unique=True, verbose_name='genre_name'
            ),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='genre_slug'),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='titles',
                to='artworks.Category',
                verbose_name='title_category',
            ),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.CharField(
                blank=True,
                max_length=200,
                null=True,
                verbose_name='title_description',
            ),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(
                blank=True,
                related_name='titles',
                to='artworks.Genre',
                verbose_name='title_genre',
            ),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=200, verbose_name='title_name'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(
                blank=True, null=True, verbose_name='title_year'
            ),
        ),
    ]