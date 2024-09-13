from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, ServiceViewSet, MechanicViewSet, LeadViewSet, DashboardViewSet, ContactInformationViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'mechanics', MechanicViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'contact', ContactInformationViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardViewSet.as_view({'get': 'statistics'})),
]
