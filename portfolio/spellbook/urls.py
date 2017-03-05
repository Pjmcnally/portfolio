from django.conf.urls import url

from .views import spell_detail, spell_list, spells, random, RandomJson

urlpatterns = [
    url(r'^$', spell_list, name='sb_spell_list'),
    url(r'^spells$', spells, name='sb_spells'),
    url(r'^spell/(?P<slug>[\w-]+)/$', spell_detail, name='sb_spell_detail'),
    # Never called but needed or the links in the main nav will break the site.
    url(r'^class/(?P<slug>[\w-]+)/$', spell_list, name='sb_class_spell_list'),
    url(r'^random/$', random, name="sb_random"),
    url(r'^random_json$', RandomJson.as_view(), name="sb_json_random"),
]
