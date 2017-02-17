from django.shortcuts import render


# Create your views here.
def temp(request):
    context = {'message':
        """This is a temporary landing pages for my Baseball project.
        This site is currently under development and will appear here once complete"""}
    return render(request, "baseball/baseball_base.html", context)
