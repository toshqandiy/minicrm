from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=13)
    address = serializers.CharField()

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance