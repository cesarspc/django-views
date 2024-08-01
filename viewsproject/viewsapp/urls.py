from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('demo/', views.index),
    path('getuser/<str:name>/<int:id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name='getform'),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
]