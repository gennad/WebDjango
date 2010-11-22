from django.conf.urls.defaults import *
from WebDjango.MainApp.views import archive

urlpatterns=patterns('', 
    url(r'^$', archive)
)