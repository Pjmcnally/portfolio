from django.conf.urls import url

from .views import temp, players

urlpatterns = [
    url(r'^$', temp, name='temp'),
    url(r'^players$', players, name='players'),
]
