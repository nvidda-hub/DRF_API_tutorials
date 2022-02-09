from django.contrib import admin
from API_1.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']