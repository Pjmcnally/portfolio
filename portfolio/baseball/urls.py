from django.conf.urls import url

from .views import temp

urlpatterns = [
    url(r'^$', temp, name='temp'),
]
