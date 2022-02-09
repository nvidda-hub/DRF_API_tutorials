from rest_framework import serializers
from API_1.models import Student



class StudentSerializer(serializers.ModelSerializer):

    def start_with_r(value):
        if value[0].lower() == 'z':
            raise serializers.ValidationError('Name should not start with z!!')

    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        
        