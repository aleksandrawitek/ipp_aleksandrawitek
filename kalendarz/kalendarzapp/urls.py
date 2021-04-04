from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.glowna, name = 'glowna'),
    path('register/', views.register, name = 'register'),
    ]
