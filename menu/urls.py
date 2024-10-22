
from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu/', views.menu, name='menu'),
    path('menu/update/', views.update_menu, name='update_menu'),
    path('<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),  # Add this line for the detail view
    path('menu/delete/<int:menu_item_id>/', views.delete_menu_item, name='delete_menu_item'),
     # other paths...
]

