from rest_framework import viewsets
from .models import Shipment, Container, CostComponent
from .serializers import ShipmentSerializer, ContainerSerializer, CostComponentSerializer

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all().order_by('-created_at')
    serializer_class = ShipmentSerializer

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

class CostComponentViewSet(viewsets.ModelViewSet):
    queryset = CostComponent.objects.all()
    serializer_class = CostComponentSerializer