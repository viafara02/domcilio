from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('estudiante/<str:pk>/', views.estudiante, name='estudiante'),
 path('ejemplo/', views.ejemplo_view, name='ejemplo'),
]