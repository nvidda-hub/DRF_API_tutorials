from API_1.models import Student
from API_1.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from API_1.custom_auth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from API_1.custom_permissions import MyPermission



class StudentModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]      # http://127.0.0.1:8000/api1/v1/viewset/students/?username=user3
    serializer_class = StudentSerializer
    queryset = Student.objects.all()