from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

    path('add_property/', views.add_property, name='add_property'),
    path('manage_property/', views.manage_property, name='manage_property'),
    
    path('edit_property/<int:id>', views.edit_property, name='edit_property'),
    path('delete_property/<int:id>', views.delete_property, name='delete_property'),

    path('property_details/<slug:slug>',
         views.property_details, name="property_details"),
    path('view_more/', views.view_more, name='view_more'),
    path('search/', views.search, name='search'),
    # path('user_property_add/', views.user_property_add, name='user_property_add'),
]
