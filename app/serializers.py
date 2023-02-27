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

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({
                'error':'age cannot be less than 18'
                })
        
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({
                'error':'name should not contain any numbers'
            })
        else:
            raise serializers.ValidationError({
                'error':'name should not be blank'
            })
        
        return data