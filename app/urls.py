from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='app_index'),
    path('login', views.login, name='app_login'),
]