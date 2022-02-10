from django.urls import path, include
from API_1 import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from API_1.custom_token import CustomAuthToken


router = DefaultRouter()


# router.register('students', views.StudentDetailViewset, basename='students')

router.register('students', views.StudentModelViewSet, basename='students')
# router.register('studentsOver', views.StudentModelViewSetOveridden, basename='studentsOver')



urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='sessionAuth')),  
    path('gettoken/', CustomAuthToken.as_view()),  
    # to provide credentials for session auth b'coz unlike basic auth there is no promopt
]

# auth token use ->  http POST http://127.0.0.1:8000/api1/v1/gettoken/ username="user2" password="userpassword2"