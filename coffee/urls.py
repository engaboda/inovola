from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoffeeMachineViewSet, CoffeePodsViewSet


coffee_router = DefaultRouter()
coffee_router.register('coffee-pods', CoffeePodsViewSet, basename='coffee_pods')
coffee_router.register('coffee-machines', CoffeeMachineViewSet, basename='coffee_machine')
