from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('create/', views.post_student_data, name='created-record'),
]