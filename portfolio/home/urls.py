from django.conf.urls import url

from .views import home, content

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^content$', content, name='content'),
    url(r'^about_me$', home, name='about_me'),
    url(r'^projects$', home, name='projects'),
    url(r'^contact$', home, name='contact'),
]
