from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('delete_user_inquiry/<int:id>', views.delete_user_inquiry, name='delete_user_inquiry'),
]
