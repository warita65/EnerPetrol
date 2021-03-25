from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.forms import FeedbackContactsForm
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/index.html")

def contact(request):
    if request.method == "POST":
        contact_form = FeedbackContactsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect(reverse("app:index"))
        else:
            print("ERROR CONTACT FORM")
    else:
        contact_form = FeedbackContactsForm()

    return render(request, "app/contact.html", {'form': contact_form})

def projects(request):
    return render(request, "app/index.html")

def services(request):
    return render(request, "app/index.html")

