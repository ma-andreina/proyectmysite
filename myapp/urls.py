from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>/', views.hello),
    path('projects/', views.projects), 
    path('tasks/<str:title>/', views.tasks),
    path('api/projects/', views.api_projects),
    path('api/tasks/', views.api_tasks),  
]