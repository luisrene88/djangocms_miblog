=====

[![Join the chat at https://gitter.im/Pyc0kw4k/djangocms_miblog](https://badges.gitter.im/Pyc0kw4k/djangocms_miblog.svg)](https://gitter.im/Pyc0kw4k/djangocms_miblog?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
djangocms_miblog
=====


Quick start
-----------

Install & settings
-------------------

1. Install the app
    ```
    pip install djangocms_miblog
    ```


2. Add "blog" to your INSTALLED_APPS setting like this
   
    ```python
    
    INSTALLED_APPS = [
        ...
        'blog',
    ]
    ```
3. Add in project URLS

    ```python
    ...
    url(r'^blog/', include('blog.urls')),
    
    ```
4. Settings Add in settings.py
    ```python
    
    BLOG_PAGINATION = 5
    BLOG_LIST_TRUNCWORDS_COUNT = 10
    
    ```

5. Migrate

  ```python
    
   ./manage.py migrate
   ```

6. Run Test Server

    ```python
    
    ./manage.py runserver
    
    ```
   
Requirements
------------

```
DjangoCMS http://www.django-cms.org/en/
django-filer & (dependencies) https://github.com/divio/django-filer
django-taggit https://github.com/alex/django-taggit
```
   

URLS
------------

```python

    urlpatterns = patterns('',
        url(r'^$', BlogPostListView.as_view(), name='post_list'),
        url(r'^(?P<slug>[-\w]+)/$', BlogPostDetailView.as_view(), name='post_detail'),
        url(r'^tag/(?P<tag>[-\w]+)/$', TaggedListView.as_view(), name='posts_tagged'),
        url(r'^category/(?P<category>[-\w]+)/$', CategoryListView.as_view(), name='posts_category'),
    )

```


Example usage
--------------

Work Models
-----------

Fields

<ul>
     <li>title [CharField]</li>
     <li>pub_date [DateTimeField]</li>
     <li>edit_date [DateTimeField]</li>
     <li>categories [ManyToMany]</li>
     <li>tags [TaggableManager()]</li>
     <li>picture [URLField]</li>
     <li>body [HTMLField]</li>
</ul>


Post List
----------

Browse post list

```Jinja
    {% for post in post_list %}
        {{post.title}}
        ...
    {% endfor %}

```


Post Detail
------------

Get Next Or Previous
<ul>
    <li>For get Next Work (Navigation) `post.get_next_post` => return (URL)</li>
    <li>For get Previous Work (Navigation) `post.get_previous_post` => return (URL)</li>
</ul>

For Get previous post
----------------------

{{post.get_previous_post}}


For Get next post
-----------------

{{post.get_next_post}}


Render post
-----------

<ul>
    <li>Title : {{post.title}}</li>
    <li>Publish at : {{post.pub_date}}</li>
    <li>Edit date : {{post.edit_date}}</li>
    <li>Categories : {% for category in post.categories.all %}{{category}}{% endfor %}</li>
    <li>Tags : {% for tag in post.tags.all %}{{tag}}{% endfor %}</li>
    <li>Picture : {{post.head_picture}}</li>
    <li>Body : {{post.body}}</li>
</ul>

Templatetags
------------

For latest post 'X is number of post'

```Jinja
    {% get_latest_post X %}

```

For get all categories

```Jinja

    {% list_post_categories %}

```

