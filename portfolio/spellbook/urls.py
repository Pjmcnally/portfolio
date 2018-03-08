from django.conf.urls import url

from .views import (spell_detail, get_spell_detail, spell_list,
    spell_list_redirect, spells, random, RandomJson)

urlpatterns = [
    # Site pages
    url(r'^$', spell_list, name='sb_spell_list'),
    url(r'^spell/(?P<slug>[\w-]+)/$', spell_detail, name='sb_spell_detail'),
    url(r'^random/$', random, name="sb_random"),

    # Depreciated link after new class search. Redirecting to main spell list.
    url(r'^class/\w*/$', spell_list_redirect, name='sb_class_spell_list'),

    # Ajax request endpoints
    url(r'^spells$', spells, name='sb_spells'),
    url(r'^get_spell_detail$', get_spell_detail, name='sb_get_spell_detail'),
    url(r'^random_json$', RandomJson.as_view(), name="sb_json_random")
]
