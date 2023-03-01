from django.contrib import admin

from .models import Student, Book, Category

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'age', 'father_name'
    ]

admin.site.register(Book)
admin.site.register(Category)