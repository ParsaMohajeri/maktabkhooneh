from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "newest posts for blog"
    link = "/rss/feed"
    description = "these are posts of blog"

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
