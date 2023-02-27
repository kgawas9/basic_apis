from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('create/', views.post_student_data, name='created-stud-record'),
    path('update/<int:id>/', views.update_student_data, name='update-stud-record'),
    path('delete/<int:id>/', views.delete_student_data, name='delete-stud-record'),
]