from django.urls import path, include
from API_1 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


# router.register('students', views.StudentDetailViewset, basename='students')

router.register('students', views.StudentModelViewSet, basename='students')
router.register('studentsOver', views.StudentModelViewSetOveridden, basename='studentsOver')



urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]