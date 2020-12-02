from django.urls import path, include
from . import views

urlpatterns = [
    path('add_realtors', views.add_realtors, name='add_realtors'),
    path('edit_realtor', views.edit_realtor, name='edit_realtor'),
    path('manage_realtors/', views.manage_realtors, name='manage_realtors'),
    path('edit_realtor/<int:id>', views.edit_realtor, name='edit_realtor'),
    path('delete_realtors/<int:id>', views.delete_realtors, name='delete_realtors'),
    path('realtor_profile/<slug:slug>', views.realtor_profile, name='realtor_profile'),
    path('all_realtors/', views.all_realtors, name='all_realtors'),
]
