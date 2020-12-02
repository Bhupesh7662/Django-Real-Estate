from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('make_inquiry/', views.make_inquiry, name='make_inquiry'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('delete_inquiry/<int:id>', views.delete_inquiry, name='delete_inquiry'),
    path('delete_feedback/<int:id>', views.delete_feedback, name='delete_feedback')
]
