from rest_framework import serializers
from .models import CoffeeMachine, CoffeePods


class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = '__all__'


class CoffeePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePods
        fields = '__all__'
