from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.glowna, name = 'glowna'),
    path('register/', views.register, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutPage, name = 'logout')
    ]
