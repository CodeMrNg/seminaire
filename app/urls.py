from django.urls import path, include
from . import views as v
from django.contrib.auth import views
from django.shortcuts import redirect


urlpatterns = [
    path('',v.home, name = 'home'),
    path('FAQ',v.faq, name = 'faq'),
    path('contact',v.contact, name = 'contact'),
]
