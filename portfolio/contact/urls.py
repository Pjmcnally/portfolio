from django.conf.urls import url
from .views import EmailMe


urlpatterns = [
    url(r'^$', EmailMe.as_view(), name='email'),
]
