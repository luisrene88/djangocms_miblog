from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.conf import settings


class BlogPostListView(ListView):
    model = Post
    template_name = 'blog/blog_post_list.html'
    paginate_by = settings.BLOG_PAGINATION
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['TRUNCWORDS_COUNT'] = settings.POSTS_LIST_TRUNCWORDS_COUNT

        return context


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'post'


class TaggedListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/blog_post_list.html'
    paginate_by = settings.BLOG_PAGINATION
    view_url_name = 'blog:posts_tagged'

    def get_queryset(self):
        qs = super(TaggedListView, self).get_queryset()
        return qs.filter(tags__slug=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        kwargs['tagged_entries'] = (self.kwargs.get('tag')
                                    if 'tag' in self.kwargs else None)
        context = super(TaggedListView, self).get_context_data(**kwargs)
        context['TRUNCWORDS_COUNT'] = settings.POSTS_LIST_TRUNCWORDS_COUNT

        return context


class CategoryListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/blog_post_list.html'
    paginate_by = settings.BLOG_PAGINATION
    view_url_name = 'blog:posts_category'

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        return qs.filter(categories__slug=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        kwargs['category'] = (self.kwargs.get('category')
                              if 'category' in self.kwargs else None)
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['TRUNCWORDS_COUNT'] = settings.POSTS_LIST_TRUNCWORDS_COUNT

        return context