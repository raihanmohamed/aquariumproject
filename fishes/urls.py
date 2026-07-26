from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fishes/', views.fish_list, name='fish_list'),
    path('fishes/add/', views.fish_create, name='fish_create'),
    path('fishes/edit/<int:pk>/', views.fish_update, name='fish_update'),
    path('fishes/delete/<int:pk>/', views.fish_delete, name='fish_delete'),
]
