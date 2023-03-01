from django.urls import path

from . import views
from .views import StudentAPI

urlpatterns = [
    # path('', views.home , name='home'),
    # path('create/', views.post_student_data, name='created-stud-record'),
    # path('update/<int:id>/', views.update_student_data, name='update-stud-record'),
    # path('delete/<int:id>/', views.delete_student_data, name='delete-stud-record'),

    path('student/', StudentAPI.as_view()),

    path('books/', views.get_books, name='get_all_books'),
]