from django.urls import path
from . import views
from .views import dashboard_redirect

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/', views.user_registration, name='registration'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),

]
