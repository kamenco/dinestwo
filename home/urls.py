from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),  # Home page view
    path('', views.customer_dashboard, name='home'),
]
