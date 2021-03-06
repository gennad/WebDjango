from django.conf.urls.defaults import *
from django.contrib.syndication.views import feed
from mainapp.views import archive
from mainapp.feeds import RSSFeed
#restapi
from django_restapi_tests.polls.models import Poll, Choice
from django_restapi.model_resource import Collection
from django_restapi.responder import XMLResponder
from django_restapi.authentication import HttpBasicAuthentication, HttpDigestAuthentication

#collections for restapi
simple_poll_resource = Collection(
    queryset = Poll.objects.all(), 
    responder = XMLResponder(),
)
simple_choice_resource = Collection(
    queryset = Choice.objects.all(),
    responder = XMLResponder()
)

#auth
basicauth_poll_resource = Collection(
    queryset = Poll.objects.all(), 
    responder = XMLResponder(),
    authentication = HttpBasicAuthentication()
)
# HTTP Digest
def digest_authfunc(username, realm):
    """
    Exemplary authfunc for HTTP Digest. In production situations,
    the combined hashes of realm, username and password are usually
    stored in an external file/db.
    """
    hashes = {
        ('realm1', 'john') : '3014aff1d0d0f0038e23c1195301def3', # Password: johnspass
        ('realm2', 'jim') : '5bae77fe607e161b831c8f8026a2ceb2'   # Password: jimspass
    }
    return hashes[(username, realm)]
digestauth_poll_resource = Collection(
    queryset = Poll.objects.all(),
    responder = XMLResponder(),
    authentication = HttpDigestAuthentication(digest_authfunc, 'realm1')
)

urlpatterns = patterns('',
    url(r'^$', archive),
    url(r'^feeds/(?P<url>.*)/$', feed, {'feed_dict': {'rss': RSSFeed}}),
    url(r'^api/poll/(.*?)/?$', simple_poll_resource),
    url(r'^api/choice/(.*?)/?$', simple_choice_resource),
    url(r'^basic/polls/(.*?)/?$', basicauth_poll_resource),
    url(r'^digest/polls/(.*?)/?$', digestauth_poll_resource),
)
