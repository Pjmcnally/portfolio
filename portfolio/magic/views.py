from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def temp(request):
    return HttpResponse(
"""This is a temporary landing pages for my Magic project.

This site is currently under development and will appear here once complete""")