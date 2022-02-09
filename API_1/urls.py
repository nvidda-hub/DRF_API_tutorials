from django.urls import path, include
from API_1 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


# router.register('students', views.StudentDetailViewset, basename='students')

router.register('students', views.StudentModelViewSet, basename='students')



urlpatterns = [
    # path('students/', views.AllStudentsView.as_view()),
    # path('students/<int:pk>/', views.StudentDetailAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('stu/', views.get_student),
    # path('stu/', views.StudentView.as_view()),
]