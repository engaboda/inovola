from rest_framework import viewsets, mixins
from .models import CoffeePods, CoffeeMachine
from .serializer import CoffeeMachineSerializer, CoffeePodsSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .utils import PRODUCT_TYPE


class CoffeePodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        list all CoffeePods 
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CoffeePodsSerializer
    queryset = CoffeePods.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('coffee_flavor', 'pack_size')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if PRODUCT_TYPE.get('{}'.format(request.query_params.get('product_type')), None):
            return Response({'results': PRODUCT_TYPE.get('{}'.format(request.query_params.get('product_type')), None)})

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CoffeeMachineViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        list all CoffeePods 
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CoffeeMachineSerializer
    queryset = CoffeeMachine.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product_type', 'water_line_compatible')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if PRODUCT_TYPE.get('{}'.format(request.query_params.get('product_type')), None):
            return Response({'results': PRODUCT_TYPE.get('{}'.format(request.query_params.get('product_type')), None)})

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
