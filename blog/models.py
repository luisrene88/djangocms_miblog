# coding: utf-8

from django.db import models
from taggit.managers import TaggableManager
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

# Reverse
from django.core.urlresolvers import reverse


class CategoryPost(models.Model):
    title = models.CharField('Titre', max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField("Titre de l'article", max_length=255)
    slug = models.SlugField()
    pub_date = models.DateTimeField('Publié le', auto_now_add=True)
    edit_date = models.DateTimeField('Dernière modification le', auto_now=True)
    categories = models.ManyToManyField(CategoryPost, verbose_name="Catégories de l'article", related_name='post_categories')
    tags = TaggableManager()
    picture = FilerImageField(verbose_name="Image d'en-tête")
    body = HTMLField(verbose_name='Article')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_publish = models.BooleanField("Publier ?", default=True)

    class Meta:
        verbose_name = 'Article de blog'
        verbose_name_plural = 'Articles de blog'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_next_post(self):
        try:
            next_post = Post.objects.get(pk=self.pk+1)
            return reverse('post_detail', args=[next_post.slug])
        except:
            return None

    def get_previous_post(self):
        try:
            previous_post = Post.objects.get(pk=self.pk-1)
            return reverse('post_detail', args=[previous_post.slug])
        except:
            return None

