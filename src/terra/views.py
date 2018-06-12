from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context = {
        "title": "Terra Bella",
        "content": " welcome to the home page. "
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": " About Page ",
        "content":" Welcome to the about page."

    }
    return render(request, "home_page.html", context)

def contact_page(request):
    context = {
        "title": " Contact Page",
        "content": "Welcome to the contact page."
    }
    if request.method == "POST":
        #print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

def home_page_old(request):
    return HttpResponse("<h1>Hello World</h1>")