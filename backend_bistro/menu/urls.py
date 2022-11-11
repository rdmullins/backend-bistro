from django.urls import path

from . import views

urlpatterns = [
    path('fullmenu', views.fullmenu, name='Return Full Menu'),
    path('appetizers', views.appetizers),
    path('breakfast', views.breakfast),
    path('brunch', views.brunch),
    path('lunch', views.lunch),
    path('dinner', views.dinner),
    path('sides', views.sides),
    path('desserts', views.desserts),
    path('eggdishes', views.eggdishes),
    path('dairy', views.dairy),
    path('menu-to-csv', views.menu_to_csv),
    path('menu-to-pdf', views.menu_to_pdf),
]