from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('',views.index, name="index"),
    path('contact',views.contact, name="contact"),
    path('about',views.about, name="about"),
    path('projects',views.projects, name="projects"),
    path('services',views.services, name="services"),

]
