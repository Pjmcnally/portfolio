from django.conf.urls import url

from . import views as v

urlpatterns = [
    # Site pages
    url(r'^$', v.spell_list, name='sb_spell_list'),
    url(r'^spell/(?P<slug>[\w-]+)/$', v.spell_detail, name='sb_spell_detail'),
    url(r'^random/$', v.random, name="sb_random"),

    # Depreciated link after new class search. Redirecting to main spell list.
    url(r'^class/\w*/$', v.spell_list_redirect, name='sb_class_spell_list'),

    # Ajax request endpoints
    url(r'^spells$', v.spells, name='sb_spells'),
    url(r'^get_spell_detail$', v.get_spell_detail, name='sb_get_spell_detail'),
    url(r'^random_json$', v.RandomJson.as_view(), name="sb_json_random")
]
