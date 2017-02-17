from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def temp(request):
    context = {'message':
        """This is a temporary landing pages for my Magic Trick project.
        This site is currently under development and will appear here once complete"""}
    return render(request, "magic/magic_base.html", context)