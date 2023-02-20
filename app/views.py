from django.shortcuts import render

# decorator api view
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerializer

from .models import Student
# Create your views here.

@api_view(['GET'])
def home(request):
    stud_obj = Student.objects.all()

    serializer = StudentSerializer(stud_obj, many=True)


    return Response({
        'status': 200,
        'payload': serializer.data,
        'message': 'Transaction successfully completed.'
    })

@api_view(['POST'])
def post_student_data(request):
    # data = request.data

    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({
            'status': 403,
            'message': 'Something went wrong',
            'error': serializer.errors
        })
    
    serializer.save()
    return Response({
        'status': 201,
        'payload': request.data,
        'message': 'New entry successfully created'
    })
