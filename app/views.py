from django.shortcuts import render

# decorator api view
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import StudentSerializer, CategorySerializer, BookSerializer

from .models import Student, Book, Category
# Create your views here.


class StudentAPI(APIView):
    def get(self, request):
        stud_obj = Student.objects.all()
        serializer = StudentSerializer(stud_obj, many=True)

        return Response({
            'status': 200,
            'message': 'Data retrieved successfully',
            'payload': serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Record successfully created',
                'payload': serializer.data
            })
        else:
            return Response({
                'status': 403,
                'message': 'Record not created'
            })

    def put(self, request):
        try:
            stud_obj = Student.objects.get(id=request.data['id'])

            serializer = StudentSerializer(stud_obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Data successfully updaetd',
                    'payload': serializer.data
                })
            else:
                return Response({
                    'status': 403,
                    'message': 'invalid request'
                })
        except Exception as e:
            return Response({
                'status': 403,
                'message': 'error - ' + str(e)
            })

    def patch(self, request):
        try:
            stud_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(stud_obj, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Record successfully updated',
                    'payload': serializer.data
                })
            else:
                return Response({
                        'status': 403,
                        'message': 'Invalid request',
                    })
        except Exception as e:
            return Response({
                'status': 403,
                'message': 'error - ' + str(e)
            })

    def delete(self, request):
        stud_obj = Student.objects.get(id=request.data['id'])
        stud_obj.delete()

        return Response({
            'status': 200,
            'message': 'Record successfully deleted'
        })












# @api_view(['GET'])
# def home(request):
#     stud_obj = Student.objects.all()

#     serializer = StudentSerializer(stud_obj, many=True)


#     return Response({
#         'status': 200,
#         'payload': serializer.data,
#         'message': 'Transaction successfully completed.'
#     })

# @api_view(['POST'])
# def post_student_data(request):
#     # data = request.data

#     serializer = StudentSerializer(data=request.data)

#     if not serializer.is_valid():
#         return Response({
#             'status': 403,
#             'message': 'Something went wrong',
#             'error': serializer.errors
#         })
    
#     serializer.save()
#     return Response({
#         'status': 201,
#         'payload': request.data,
#         'message': 'New entry successfully created'
#     })

# @api_view(['PUT'])
# def update_student_data(request, id):
#     try:
#         student_obj = Student.objects.get(pk=id)
    
#         data = request.data

#         serializer = StudentSerializer(student_obj, data=data)

#         if not serializer.is_valid():
#             return Response({
#                 'status': 403,
#                 'error': serializer.errors,
#                 'message': 'invalid input'
#             })
        
#         serializer.save()
#         return Response({
#             'status': 200,
#             'payload': serializer.data,
#             'message': 'Data successfully updated - put request'
#         })
    
#     except Exception as e:
#         return Response({
#             'status': 403,
#             'error': 'invalid id' + str(e)
#         })

# @api_view(['PATCH'])
# def update_student_data(request, id):
#     try:
#         student_obj = Student.objects.get(pk=id)
    
#         data = request.data

#         serializer = StudentSerializer(student_obj, data=data, partial = True)

#         if not serializer.is_valid():
#             return Response({
#                 'status': 403,
#                 'error': serializer.errors,
#                 'message': 'invalid input'
#             })
        
#         serializer.save()
#         return Response({
#             'status': 200,
#             'payload': serializer.data,
#             'message': 'Data successfully updated - patch request'
#         })
    
#     except Exception as e:
#         return Response({
#             'status': 403,
#             'error': 'invalid id' + str(e)
#         })


# @api_view(['DELETE'])
# def delete_student_data(request, id):
#     try:
#         stud_obj = Student.objects.get(id=id)
#         stud_obj.delete()

#         return Response({
#             'status': 200,
#             'message': 'record delete'
#         })
#     except Exception as e:
#         return Response({
#             'status': 403,
#             'message': 'Unable to delete record ' + str(e)
#         })
    

@api_view(['GET'])
def get_books(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)

    return Response({
            'status': 200,
            'payload': serializer.data
        })
