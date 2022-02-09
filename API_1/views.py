from functools import partial
from django.http import JsonResponse
from itsdangerous import Serializer
from API_1.models import Student
from API_1.serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from django.views import View
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView

from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from rest_framework import serializers, status
from rest_framework.response import Response

from rest_framework import viewsets

# Create your views here.

# API views 

# funtcion based views without api_view()

# def studentDetailView(request, pk):
#     student_obj = Student.objects.get(id=pk)
#     serializer = StudentSerializer(student_obj)
#     return JsonResponse(serializer.data)

# def studentsView(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(student_obj, many=True)
#     return JsonResponse(serializer.data, safe=False)


# third party app views
# to get data
# @csrf_exempt
# def get_student(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')

#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata) # converting complex data

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data posted successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         id = pythondata.get('id')
#         updated_student_data = Student.objects.get(id=id)

#         # for partial update
#         serializer = StudentSerializer(updated_student_data, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data updated successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    

#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         if id:
#             student = Student.objects.get(id=id)
#             student.delete()
#             res = {'msg':f'id : {id}, student data deleted'}
#             json_data = JSONRenderer().render(json_data)
#             return HttpResponse(json_data, content_type="application/json")

#         res = {'msg':'Student id does not exist !!!'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res, safe=False)


# class based view without api_view()

# @method_decorator(csrf_exempt, name='dispatch')
# class StudentView(View):
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')

#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
    

#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata) # converting complex data

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data posted successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         id = pythondata.get('id')
#         updated_student_data = Student.objects.get(id=id)

#         # for partial update
#         serializer = StudentSerializer(updated_student_data, data=pythondata, partial=True)

#         # for complete update
#         serializer = StudentSerializer(updated_student_data, data=pythondata)
        
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data updated successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         if id:
#             student = Student.objects.get(id=id)
#             student.delete()
#             res = {'msg':f'id : {id}, student data deleted'}
#             json_data = JSONRenderer().render(json_data)
#             return HttpResponse(json_data, content_type="application/json")

#         res = {'msg':'Student id does not exist !!!'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res, safe=False) 


# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def studentDetailAPIView(request, pk=None):
#     if request.method == 'GET':
#         if pk:
#             try:
#                 student_obj = Student.objects.get(pk=pk)
#             except:
#                 return Response({"msg":f"Record for id {pk} Not found!!"})

#             serializer = StudentSerializer(student_obj)
#             return Response(serializer.data, status=status.HTTP_200_OK)
    

#     if request.method == 'PUT':
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':f'id {pk} Data updated successfully!'}, status=status.HTTP_226_IM_USED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'PATCH':
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':f'id : {pk} patially Data updated successfully!'}, status=status.HTTP_226_IM_USED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         student = Student.objects.get(pk=pk)
#         student.delete()
#         return Response({"msg":f"data of student with id {pk} deleted!!"})


# @api_view(['GET', 'POST'])
# def studentsAPIView(request):
#     if request.method == 'GET':
#         student_obj = Student.objects.all()
#         serializer = StudentSerializer(student_obj, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated successfully!'})
#         return Response(serializer.errors)



# APIView


# class StudentDetailAPIView(APIView):
#     def get(self, request, pk, format=None):
#         if pk:
#             try:
#                 student_obj = Student.objects.get(pk=pk)
#             except:
#                 return Response({"msg":f"Record for id {pk} Not found!!"})

#             serializer = StudentSerializer(student_obj)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk, format=None):            
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':f'id {pk} Data updated successfully!'}, status=status.HTTP_226_IM_USED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk, format=None):
#         try:
#             student = Student.objects.get(pk=pk)
#         except:
#             return Response({"msg":f"data of student with id {pk} not found!!"})
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':f'id : {pk} patially Data updated successfully!'}, status=status.HTTP_226_IM_USED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         try:
#             student = Student.objects.get(pk=pk)
#         except:
#             return Response({"msg":f"data of student with id {pk} not found!!"})

#         student.delete()
#         return Response({"msg":f"data of student with id {pk} deleted!!"})


# class StudentAPIView(APIView):
#     def get(self, request, format=None):
#         student_obj = Student.objects.all()
#         serializer = StudentSerializer(student_obj, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data updated successfully!'})


# GenericView API

# class StudentDetailAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()

#     def get(self, request, pk=None, *args, **kwargs):
#         if pk:
#             return self.retrieve(request)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, pk=None, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# class AllStudentsView(GenericAPIView, ListModelMixin):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)



# view sets


# class StudentDetailViewset(viewsets.ViewSet):
#     def list(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         if pk:
#             student = Student.objects.get(pk=pk)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Student data added"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response({"msg":"Student data updated"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response({"msg":"Student data updated"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         student.delete()
#         return Response({"msg":"Data deleted"})


# ModelViewSet

class StudentModelViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()