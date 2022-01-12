from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from blog.models import Page


def home(request):
    return render(request, "blog/index.html")


def pages(request):
    blogs = Page.objects.all()
    print(blogs)
    return render(request, "blog/pages.html", {"blogs": blogs})


def page(request, id):

    blog = Page.objects.get(pk=id)

    return render(request, "blog/page.html", {"blog": blog})


def login(request):
    return render(request, "blog/login.html")


def signup(request):
    return HttpResponse("Vista Entrenador.")


def about(request):
    return render(request, "blog/about.html")
