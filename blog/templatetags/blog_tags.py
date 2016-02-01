# coding: utf-8

#Import Models

from blog.models import CategoryPost, Post

# import template for register
from django import template

register = template.Library()


@register.inclusion_tag('blog/tags/latest_posts.html')
def get_latest_post(numbers_of_post):
    latest_posts = Post.objects.filter(is_publish=True).order_by('-pub_date')[:numbers_of_post]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('blog/tags/post_categories.html')
def list_post_categories():
    categories = CategoryPost.objects.filter(is_publish=True).order_by('title')
    return {'categories': categories}

