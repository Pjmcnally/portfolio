"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from spellbook import urls as spellbook_urls
from home import urls as home_urls
from baseball import urls as baseball_urls
from lol_app import urls as lol_app_urls
from contact import urls as contact_urls
from user import urls as user_urls

urlpatterns = [
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^admin/', admin.site.urls),
    url(r'^spellbook/', include(spellbook_urls)),
    url(r'^lol_app/', include(lol_app_urls)),
    url(r'^baseball/', include(baseball_urls)),
    url(r'^email/', include(contact_urls)),
    url(r'^user/', include(user_urls, app_name='user', namespace='dj-auth')),
    url(r'^', include(home_urls)),
]
