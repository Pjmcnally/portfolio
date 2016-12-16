from django.conf.urls import url

from .views import spell_detail, spell_page, spell_content

urlpatterns = [
    url(r'^$', spell_page, name='sb_spell_page'),
    url(r'^spell_content$', spell_content, name='spell_content'),
    url(r'^spell/(?P<slug>[\w-]+)/$', spell_detail, name='spell_detail'),
    # Never called but needed or the links in the main nav will break the site.
    url(r'^class/(?P<slug>[\w-]+)/$', spell_page, name='class_spell_list'),
]
