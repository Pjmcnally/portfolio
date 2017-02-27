from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def home(request):
    return render(request, 'home/home_base.html', {})


def content(request):
    if request.method == 'POST':
        page = request.POST.get("page", None)

    return render(request, "home{}.html".format(page))
