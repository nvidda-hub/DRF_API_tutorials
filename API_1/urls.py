from django.urls import path, include
from API_1 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()


# router.register('students', views.StudentDetailViewset, basename='students')

router.register('students', views.StudentModelViewSet, basename='students')
# router.register('studentsOver', views.StudentModelViewSetOveridden, basename='studentsOver')



urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='sessionAuth')),  
    path('gettoken/', obtain_auth_token),  
    # to provide credentials for session auth b'coz unlike basic auth there is no promopt
]