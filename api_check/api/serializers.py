from rest_framework import serializers

from api.models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def create(self, validate_date):
        print(validate_date)
        return Student.objects.create(**validate_date)

    def update(self, instance, validate_date):
        instance.name = validate_date.get('name', instance.name)
        instance.age = validate_date.get('age', instance.age)
        instance.address = validate_date.get('address', instance.address)
        instance.save()
        return instance
