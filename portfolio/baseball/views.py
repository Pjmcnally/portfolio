from django.shortcuts import render
from .models import Player


# Create your views here.
def temp(request):
    context = {'message':
        """This is a temporary landing pages for my Baseball project.
        This site is currently under development and will appear here once complete"""}
    return render(request, "baseball/baseball_base.html", context)


def players(request):
    context = {'players': Player.objects.all()}
    return render(request, "baseball/players.html", context)
