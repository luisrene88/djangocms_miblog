# coding: utf-8

#Import Models

from blog.models import CategoryPost, Post
from django import template

register = template.Library()


@register.inclusion_tag('blog/tags/latest_posts.html')
def get_latest_post(numbers_of_post):
    latest_posts = Post.objects.all().order_by('-pub_date')[:numbers_of_post]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('blog/tags/post_categories.html')
def list_post_categories():
    categories = CategoryPost.objects.all().order_by('title')
    return {'categories': categories}

