from rest_framework import serializers
from API_1.models import Student


# # writting validators
# def start_with_r(value):
#     if value[0].lower() != 'z':
#         raise serializers.ValidationError('Name should not start with z!!')

# def roll_validator(value):
#     if value >= 200:
#         raise serializers.ValidationError('Keep roll below 200!!')

# def city_validator(value):
#     if value.lower() == 'city':
#         raise serializers.ValidationError('name your city!!')


# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50,validators=[start_with_r])
#     roll = serializers.IntegerField(validators=[roll_validator])
#     city = serializers.CharField(max_length=50,validators=[city_validator])

#     # inserting data
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     # for updating data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
    
#     # Field level Validation
#     # def validate_roll(self, value):
#     #     if value >= 200:
#     #         raise serializers.ValidationError("Seat Full")
#     #     return value
    
#     # object level validation
#     # def validate(self, data):
#     #     name_check = data.get('name')
#     #     city_check = data.get('city')
#     #     if name_check.lower() == 'student' and city_check.lower() != 'city':
#     #         raise serializers.ValidationError('student must have valid name and city name!!')
#     #     return data


class StudentSerializer(serializers.ModelSerializer):

    def start_with_r(value):
        if value[0].lower() == 'z':
            raise serializers.ValidationError('Name should not start with z!!')

    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        
        