from django.conf.urls.defaults import *
from django.contrib.syndication.views import feed
from mainapp.views import archive
from mainapp.feeds import RSSFeed
#restapi
from django_restapi.model_resource import Collection
from django_restapi.responder import XMLResponder

#collections for restapi
simple_poll_resource = Collection(
    queryset = Poll.objects.all(), 
    responder = XMLResponder(),
)
simple_choice_resource = Collection(
    queryset = Choice.objects.all(),
    responder = XMLResponder()
)

urlpatterns = patterns('',
    url(r'^$', archive),
    url(r'^feeds/(?P<url>.*)/$', feed, {'feed_dict': {'rss': RSSFeed}}),
    url(r'^api/poll/(.*?)/?$', simple_poll_resource),
    url(r'^api/choice/(.*?)/?$', simple_choice_resource),
)
