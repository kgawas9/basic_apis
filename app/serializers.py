from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name', 'age', 'father_name'
        ]
        # exlcude = ['']
        # fields = '__all__'
