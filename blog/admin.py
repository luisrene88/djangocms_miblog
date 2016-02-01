# coding: utf-8

from django.contrib import admin
from .models import CategoryPost, Post
from django import forms


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        wtf = CategoryPost.objects.all()
        w = self.fields['categories'].widget
        choices = []
        for choice in wtf:
            choices.append((choice.id, choice.title))
        w.choices = choices


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pub_date', 'edit_date', 'get_categories', 'is_publish')
    list_filter = ('title', 'pub_date', 'edit_date', 'is_publish')
    list_editable = ('is_publish',)
    filter_horizontal = ('categories',)
    form = PostForm
    fieldsets = (
        ('Information', {
            'fields': ('title', 'slug', 'categories', 'tags', 'picture' )
        }),
        ('Rédaction', {
            'fields': ('body', )
        }),
        ('Publication', {
            'fields': ('start_date', 'end_date', 'is_publish',)
        }),
    )

    def get_categories(self, obj):
        return "\n".join([p.title for p in obj.categories.all()])


class CategoryPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(CategoryPost, CategoryPostAdmin)

