from django.conf.urls import url

from .views import spell_detail, spell_page, spells

urlpatterns = [
    url(r'^$', spell_page, name='sb_spell_page'),
    url(r'^spells$', spells, name='sb_spells'),
    url(r'^spell/(?P<slug>[\w-]+)/$', spell_detail, name='sb_pell_detail'),
    # Never called but needed or the links in the main nav will break the site.
    url(r'^class/(?P<slug>[\w-]+)/$', spell_page, name='class_spell_list'),
]
