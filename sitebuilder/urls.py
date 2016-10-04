from django.conf.urls import include, url

from .views import page


urlpatterns = (
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    url(r'^$', page, name='homepage'),
    url(r'^scribbler/', include('scribbler.urls')),
)