from API_1.models import Student
from API_1.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()