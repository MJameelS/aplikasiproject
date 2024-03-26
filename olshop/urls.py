from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.landing, name='home'),
    path('<int:id>', views.detail_view, name = 'detail_view'),
    path('contact/', views.contact, name = 'contact'),
    path('review/', views.review, name = 'review'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
]