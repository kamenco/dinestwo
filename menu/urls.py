
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu/', views.menu, name='menu'),
    path('menu/update/', views.update_menu, name='update_menu'),
    # other paths...
]

