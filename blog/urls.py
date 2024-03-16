from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
# from blog.feeds import LatestEntriesFeed
app_name = 'blog'

urlpatterns = [
    path('',blog_view, name='index'),
    # path('single/',blog_single, name='single'),
    path('<int:pid>',blog_single, name='single'),
    # path('category/<str:cat_name>',blog_view, name='category'),
    # path('tag/<str:tag_name>',blog_view, name='tag'),
    # path('author/<str:author_username>',blog_view,name='author'),
    # path('search/',blog_search,name='search'),
    # path('post-<int:pid>',test, name='test'), 
    # path("rss/feed/", LatestEntriesFeed()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)