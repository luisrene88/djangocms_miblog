# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields
import filer.fields.image
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Titre', max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Post title', max_length=255)),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Published on')),
                ('edit_date', models.DateTimeField(verbose_name='Edit on', auto_now=True)),
                ('body', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Post')),
                ('is_publish', models.BooleanField(verbose_name='is publish ?', default=True)),
                ('categories', models.ManyToManyField(verbose_name='Catégories', related_name='post_categories', to='blog.CategoryPost')),
                ('picture', filer.fields.image.FilerImageField(verbose_name='Head picture', to='filer.Image')),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.')),
            ],
            options={
                'verbose_name': 'Blog post',
                'verbose_name_plural': 'Blog posts',
            },
        ),
    ]
