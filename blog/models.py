# coding: utf-8

# Django DB
from django.db import models

# Django Taggit
from taggit.managers import TaggableManager

# Django CKEditor
from djangocms_text_ckeditor.fields import HTMLField

# Django Filer
from filer.fields.image import FilerImageField

# Reverse
from django.core.urlresolvers import reverse

# I18N
from django.utils.translation import ugettext as _


class CategoryPost(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Post title"), max_length=255)
    slug = models.SlugField()
    pub_date = models.DateTimeField(_('Published on'), auto_now_add=True)
    edit_date = models.DateTimeField(_('Edit on'), auto_now=True)
    categories = models.ManyToManyField(CategoryPost, verbose_name=_("Categories"), related_name='post_categories')
    tags = TaggableManager()
    picture = FilerImageField(verbose_name=_("Head picture"))
    body = HTMLField(verbose_name=_('Post'))
    is_publish = models.BooleanField(_("is publish ?"), default=True)

    class Meta:
        verbose_name = _('Blog post')
        verbose_name_plural = _('Blog posts')

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

