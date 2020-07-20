from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:session_name>/', views.session, name='session'),
]