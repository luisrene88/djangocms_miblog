from django.conf.urls import *
from .views import BlogPostListView, BlogPostDetailView, TaggedListView, CategoryListView

urlpatterns = patterns('',
    url(r'^$', BlogPostListView.as_view(), name='post_list'),
    url(r'^(?P<slug>[-\w]+)/$', BlogPostDetailView.as_view(), name='post_detail'),
    url(r'^tag/(?P<tag>[-\w]+)/$', TaggedListView.as_view(), name='posts_tagged'),
    url(r'^category/(?P<category>[-\w]+)/$', CategoryListView.as_view(), name='posts_category'),
)