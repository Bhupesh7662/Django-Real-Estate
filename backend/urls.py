from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='dashboard_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
