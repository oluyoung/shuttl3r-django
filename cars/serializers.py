from rest_framework import serializers
from .models import CarOrder


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarOrder
        fields = '__all__'
