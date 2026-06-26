from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipmentViewSet, ContainerViewSet, CostComponentViewSet

router = DefaultRouter()
router.register(r'shipments', ShipmentViewSet)
router.register(r'containers', ContainerViewSet)
router.register(r'costs', CostComponentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]