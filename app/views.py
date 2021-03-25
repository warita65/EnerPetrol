from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/index.html")

def contact(request):
    return render(request, "app/index.html")

def projects(request):
    return render(request, "app/index.html")

def services(request):
    return render(request, "app/index.html")

