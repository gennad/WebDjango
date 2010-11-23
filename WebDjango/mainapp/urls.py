from django.conf.urls.defaults import *
from django.contrib.syndication.views import feed
from mainapp.views import archive
from mainapp.feeds import RSSFeed

urlpatterns = patterns('',
    url(r'^$', archive),
    url(r'^feeds/(?P<url>.*)/$', feed, {'feed_dict': {'rss': RSSFeed}}),
)
