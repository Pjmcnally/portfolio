from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from random import choice
from portfolio import local_settings
import json
from distutils import util


from .models import Clss, Spell


@ensure_csrf_cookie
def spell_list(request):
    """ function to render spell list page """

    # get all classes for class search section
    context = {'classes': Clss.objects.all()}
    return render(request, 'spellbook/spell_list.html', context)

def spell_list_redirect(request):
    return redirect('sb_spell_list')


def spell_detail(request, slug):
    spell = Spell.objects.get(slug=slug)
    context = {'spell': spell}
    return render(request, 'spellbook/spell_detail.html', context)

def get_spell_detail(request):
    # If not post request reject
    if request.method != 'POST':
        return HttpResponse("")

    spell_slug = request.POST.get("spell", None)
    if not spell_slug:
        return HttpResponse("")

    spell = Spell.objects.get(slug=spell_slug)
    context = {'spell': spell}
    return render(request, 'spellbook/get_spell_detail.html', context)


def spells(request):
    # If not post request reject
    if request.method != 'POST':
        return HttpResponse("")

    spells = Spell.objects.filter(source__public=True)

    clss_include = request.POST.get("class_inc").split()
    if clss_include:
        print("including")
        include = Q()
        for clss in clss_include:
            include |= Q(clss__slug__contains=clss)
        spells = spells.filter(include).distinct()

    clss_exclude = request.POST.get("class_exc").split()
    if clss_exclude:
        exclude = Q()
        for clss in clss_exclude:
            exclude |= Q(clss__slug__contains=clss)
        spells = spells.exclude(exclude)

    # ritual will either be "true", "false" or ""(empty string)
    ritual = request.POST.get("rit", None)
    if ritual:
        rit_bool = util.strtobool(ritual)
        spells = spells.filter(ritual=rit_bool)

    # conc will either be "true", "false" or ""(empty string)
    conc = request.POST.get("con", None)
    if conc:
        conc_bool = util.strtobool(conc)
        spells = spells.filter(concentration=conc_bool)

    # The next 3 sections are for the 3 components V, S, M
    # com_v will either be "true", "false" or ""(empty string)
    com_v = request.POST.get("com_v", None)
    if com_v == "true":
        spells = spells.filter(component__short_name__contains="v")
    elif com_v == "false":
        spells = spells.exclude(component__short_name__contains="v")

    # com_s will either be "true", "false" or ""(empty string)
    com_s = request.POST.get("com_s", None)
    if com_s == "true":
        spells = spells.filter(component__short_name__contains="s")
    elif com_s == "false":
        spells = spells.exclude(component__short_name__contains="s")

    # com_m either be "true", "false" or ""(empty string)
    com_m = request.POST.get("com_m", None)
    if com_m == "true":
        spells = spells.filter(component__short_name__contains="m")
    elif com_m == "false":
        spells = spells.exclude(component__short_name__contains="m")

    search = request.POST.get("search", None)
    if search:
        spells = spells.filter(name__icontains=search)

    if spells:
        spell_dict = {
            0: spells.filter(level__num=0),
            1: spells.filter(level__num=1),
            2: spells.filter(level__num=2),
            3: spells.filter(level__num=3),
            4: spells.filter(level__num=4),
            5: spells.filter(level__num=5),
            6: spells.filter(level__num=6),
            7: spells.filter(level__num=7),
            8: spells.filter(level__num=8),
            9: spells.filter(level__num=9),
        }

        context = {
            'spells': spell_dict}

        return render(request, 'spellbook/spells.html', context)

    else:
        return HttpResponse("No spells found!")


def random(request):
    """ Function to redirect to random spell page """
    r = RandomJson.as_view()(request)
    json_data = json.loads(r.content.decode('utf-8'))
    return redirect("sb_spell_detail", json_data["slug"])


@method_decorator(csrf_exempt, name="dispatch")
class RandomJson(View):
    def get(self, request):
        spell = choice(Spell.objects.all().filter(source__public=True))
        spell_obj = {
            'name': spell.name,
            'url': spell.get_absolute_url(),
            'slug': spell.slug}
        return JsonResponse(spell_obj)

    def post(self, request):
        if request.POST.get('key') != local_settings.TWITTERBOT_KEY:  # simple attempt at security
            return None

        spell = None

        while not spell:
            spells = Spell.objects.all().filter(source__public=True).filter(tweeted=False)

            if spells:
                spell = choice(spells)
            else:  # If all spells have been tweeted reset them all
                for spell in Spell.objects.all().filter(source__public=True):
                    spell.tweeted = False
                    spell.save()

        if request.POST.get('track'):
            spell.tweeted = True
            spell.save()

        spell_obj = {
            'name': spell.name,
            'url': spell.get_absolute_url(),
            'slug': spell.slug}
        return JsonResponse(spell_obj)
