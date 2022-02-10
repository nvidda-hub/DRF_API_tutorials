from API_1.models import Student
from API_1.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from API_1.custom_auth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from API_1.custom_permissions import MyPermission
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from API_1.custom_throttling import CustomThrottlingForUser
from django_filters.rest_framework import DjangoFilterBackend



class StudentModelViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]      # http://127.0.0.1:8000/api1/v1/viewset/students/?username=user3
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']
