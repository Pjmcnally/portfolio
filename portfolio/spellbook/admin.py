from django.contrib import admin
from .models import (CastingTime, Clss, Component, Domain, Duration, Level,
                     Range, School, Source, SpellSource, SubDomain, Spell)

# Register your models here.
admin.site.register(CastingTime)
admin.site.register(Clss)
admin.site.register(Component)
admin.site.register(Domain)
admin.site.register(Duration)
admin.site.register(Level)
admin.site.register(Range)
admin.site.register(School)
admin.site.register(Source)
admin.site.register(SpellSource)
admin.site.register(SubDomain)
admin.site.register(Spell)
