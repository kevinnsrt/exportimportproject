from rest_framework import serializers
from .models import Shipment, Container, CostComponent

class CostComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostComponent
        fields = '__all__'

class ContainerSerializer(serializers.ModelSerializer):
    costs = CostComponentSerializer(many=True, read_only=True)

    class Meta:
        model = Container
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    containers = ContainerSerializer(many=True, read_only=True)
    total_cost = serializers.ReadOnlyField(source='total_administrative_cost')

    class Meta:
        model = Shipment
        fields = ['id', 'bl_number', 'transaction_type', 'shipper', 'consignee', 
                  'origin_port', 'destination_port', 'status', 'total_cost', 
                  'containers', 'created_at']