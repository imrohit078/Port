from django.urls import path, include
from my_app import views

urlpatterns = [
    path('', views.home)
    
]
