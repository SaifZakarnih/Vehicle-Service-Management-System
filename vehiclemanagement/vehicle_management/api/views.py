import pdb

from rest_framework import viewsets
from ..models import Vehicle, Service, Mechanic, Lead, ContactInformation
from ..serializers import VehicleSerializer, ServiceSerializer, MechanicSerializer, LeadSerializer, \
    ContactInformationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(detail=True, methods=['get'])
    def total_service_cost(self, request, pk=None):
        vehicle = self.get_object()
        total_cost = vehicle.service_set.aggregate(Sum('cost'))['cost__sum']
        return Response({'total_cost': total_cost})


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    @action(detail=False, methods=['get'])
    def top_expensive_services(self, request):
        top_services = Service.objects.order_by('-cost')[:5]
        serializer = self.get_serializer(top_services, many=True)
        return Response(serializer.data)


class MechanicViewSet(viewsets.ModelViewSet):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer

    @action(detail=False, methods=['get'])
    def count_by_specialization(self, request):
        specialization_counts = Mechanic.objects.values('specialization').annotate(total=Count('id'))
        return Response(specialization_counts)

    @action(detail=True, methods=['get'])
    def vehicles_serviced(self, request, pk=None):
        mechanic = self.get_object()
        vehicles = Vehicle.objects.filter(service__in=mechanic.services.all()).distinct()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class ContactInformationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer


class DashboardViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        total_service_cost = Service.objects.aggregate(Sum('cost'))['cost__sum']
        services_by_date = Service.objects.values('date').annotate(total_cost=Sum('cost'))
        leads_by_day = Lead.objects.extra(select={'day': "date(creation_date)"}).values('day').annotate(
            count=Count('id'))

        return Response({
            'total_service_cost': total_service_cost,
            'services_by_date': services_by_date,
            'leads_by_day': leads_by_day
        })
