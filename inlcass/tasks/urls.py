from django.urls import path 
from . import views 

app_name = 'tasks'

urlpatterns = [
    path('tasks/', views.index, name='index'),
    path('tasks/add', views.add, name='add'),
]

