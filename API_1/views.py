from API_1.models import Student
from API_1.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from API_1.custom_auth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from API_1.custom_permissions import MyPermission


# For Basic Authentication


# class StudentModelViewSet(viewsets.ModelViewSet):
#     # gives out permissions this way if we have few classes to give permission
#     # other wise define globally means writeout in settings.py
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()

# class StudentModelViewSetOveridden(viewsets.ModelViewSet):
#     # gives out permissions this way if we have few classes to give permission
#     # other wise define globally means writeout in settings.py
#     # authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()



# sesssion authentication

class StudentModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]      # http://127.0.0.1:8000/api1/v1/viewset/students/?username=user3
    serializer_class = StudentSerializer
    queryset = Student.objects.all()