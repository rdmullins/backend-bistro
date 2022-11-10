from django.urls import path

from . import views

urlpatterns = [
    path('fullmenu', views.fullmenu, name='Return Full Menu'),
]