from rest_framework import serializers

from .models import Student, Category, Book

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name', 'age', 'father_name'
        ]

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
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'category_name'
        ]


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = [
            'id', 'book_title', 'category'
        ]
        # depth = 1
