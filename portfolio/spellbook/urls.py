from django.conf.urls import url

from .views import (spell_detail, spell_list, spell_list_redirect, spells,
    random, RandomJson)

urlpatterns = [
    url(r'^$', spell_list, name='sb_spell_list'),
    url(r'^spells$', spells, name='sb_spells'),
    url(r'^spell/(?P<slug>[\w-]+)/$', spell_detail, name='sb_spell_detail'),
    # Depreciated link after new class search. Redirecting to main spell list.
    url(r'^class/\w*/$', spell_list_redirect, name='sb_class_spell_list'),
    url(r'^random/$', random, name="sb_random"),
    url(r'^random_json$', RandomJson.as_view(), name="sb_json_random"),
]
