from django.test import TestCase

from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from . import models
from . import serializers
import datetime


class VehicleAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.vehicle_data = {
            'vin': '1HGCM82633A123456',
            'make': 'Honda',
            'model': 'Civic',
            'year': 2018
        }
        self.vehicle = models.Vehicle.objects.create(**self.vehicle_data)

    def test_create_vehicle(self):
        response = self.client.post(reverse('vehicle-list'), self.vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['vin'], '1HGCM82633A123456')

    def test_get_vehicle(self):
        response = self.client.get(reverse('vehicle-detail', kwargs={'pk': self.vehicle.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vin'], '1HGCM82633A123456')
        self.assertEqual(response.data['make'], 'Honda')

    def test_update_vehicle(self):
        updated_data = {
            'vin': '1HGCM82633A789101',
            'make': 'Toyota',
            'model': 'Camry',
            'year': 2021
        }
        response = self.client.put(reverse('vehicle-detail', kwargs={'pk': self.vehicle.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['vin'], '1HGCM82633A789101')
        self.assertEqual(response.data['make'], 'Toyota')

    def test_partial_update_vehicle(self):
        updated_data = {'make': 'Ford'}
        response = self.client.patch(reverse('vehicle-detail', kwargs={'pk': self.vehicle.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['make'], 'Ford')

    def test_delete_vehicle(self):
        response = self.client.delete(reverse('vehicle-detail', kwargs={'pk': self.vehicle.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Vehicle.objects.filter(pk=self.vehicle.pk).exists())


class ServiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vehicle = models.Vehicle.objects.create(vin='1HGCM82633A654321', make='Ford', model='Fusion', year=2015)
        self.service_data = {
            'vehicle': self.vehicle.id,
            'description': 'Engine repair',
            'cost': 350.00,
            'date': '2024-01-01'
        }

    def test_create_service(self):
        response = self.client.post(reverse('service-list'), self.service_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_service(self):
        service = self.client.post(reverse('service-list'), self.service_data, format='json')
        self.assertEqual(service.status_code, status.HTTP_201_CREATED)
        response = self.client.get(reverse('service-detail', kwargs={'pk': service.data.get('id')}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Engine repair')
        self.assertEqual(response.data['cost'], 350.0)
        self.assertEqual(response.data['date'], '2024-01-01')


class LeadAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.vehicle_data = {
            'vin': '1HGCM82633A123456',
            'make': 'Honda',
            'model': 'Civic',
            'year': 2018
        }
        self.vehicle = models.Vehicle.objects.create(**self.vehicle_data)
        self.vehicle_data2 = {
            'vin': '2HGCM82633A123456',
            'make': 'Honda',
            'model': 'Civic',
            'year': 2018
        }
        self.vehicle2 = models.Vehicle.objects.create(**self.vehicle_data)
        self.lead_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '555-1234',
            'vehicles': [self.vehicle.pk, self.vehicle2.pk]
        }

    def test_create_lead(self):
        response = self.client.post(reverse('lead-list'), self.lead_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], 'John')

    def test_get_lead(self):
        lead = self.client.post(reverse('lead-list'), self.lead_data, format='json')
        self.assertEqual(lead.status_code, status.HTTP_201_CREATED)
        response = self.client.get(reverse('lead-detail', kwargs={'pk': lead.data.get('id')}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')
        self.assertEqual(response.data['last_name'], 'Doe')

    def test_update_lead(self):
        self.vehicle_data = {
            'vin': '1HGCM82633A123456',
            'make': 'Honda',
            'model': 'Civic',
            'year': 2018
        }
        self.vehicle = models.Vehicle.objects.create(**self.vehicle_data)
        self.vehicle_data2 = {
            'vin': '2HGCM82633A123456',
            'make': 'Honda',
            'model': 'Civic',
            'year': 2018
        }
        self.vehicle2 = models.Vehicle.objects.create(**self.vehicle_data)
        updated_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'phone': '555-5678',
            'vehicles': [self.vehicle.pk, self.vehicle2.pk]
        }
        lead = self.client.post(reverse('lead-list'), self.lead_data, format='json')
        self.assertEqual(lead.status_code, status.HTTP_201_CREATED)
        response = self.client.put(reverse('lead-detail', kwargs={'pk': lead.data.get('id')}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')
        self.assertEqual(response.data['last_name'], 'Smith')

    def test_partial_update_lead(self):
        updated_data = {'first_name': 'Johnny'}
        lead = self.client.post(reverse('lead-list'), self.lead_data, format='json')
        self.assertEqual(lead.status_code, status.HTTP_201_CREATED)
        response = self.client.patch(reverse('lead-detail', kwargs={'pk': lead.data.get('id')}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Johnny')

    def test_delete_lead(self):
        lead = self.client.post(reverse('lead-list'), self.lead_data, format='json')
        self.assertEqual(lead.status_code, status.HTTP_201_CREATED)
        response = self.client.delete(reverse('lead-detail', kwargs={'pk': lead.data.get('id')}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Lead.objects.filter(pk=lead.data.get('id')).exists())


class TopServicesTestCase(TestCase):

    def setUp(self):
        self.vehicle = models.Vehicle.objects.create(make="Toyota", model="Corolla", year=2000, vin='totallyrealvin')

        models.Service.objects.create(vehicle=self.vehicle, description="Oil Change", cost=100.0, date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Tire Replacement", cost=200.0, date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Brake Inspection", cost=300.0, date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Battery Replacement", cost=400.0, date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Transmission Repair", cost=500.0, date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Engine Overhaul", cost=600.0, date=datetime.datetime.now())

    def test_top_expensive_services(self):
        response = self.client.get('/services/top_expensive_services/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_services = models.Service.objects.order_by('-cost')[:5]
        serializer = serializers.ServiceSerializer(expected_services, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_top_expensive_services_empty(self):
        models.Service.objects.all().delete()

        response = self.client.get('/services/top_expensive_services/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, [])

    def test_top_expensive_services_ordering(self):
        models.Service.objects.create(vehicle=self.vehicle, description="New Service 1", cost=400.0, date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="New Service 2", cost=300.0, date=datetime.datetime.now())

        response = self.client.get('/services/top_expensive_services/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_services = models.Service.objects.order_by('-cost')[:5]
        serializer = serializers.ServiceSerializer(expected_services, many=True)
        self.assertEqual(response.data, serializer.data)


class TotalCostTestCase(TestCase):
    def setUp(self):
        self.vehicle = models.Vehicle.objects.create(make="Toyota", model="Corolla", year=2000, vin='totallyrealvin')

        models.Service.objects.create(vehicle=self.vehicle, description="Oil Change", cost=100.0,
                                      date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Tire Replacement", cost=200.0,
                                      date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Brake Inspection", cost=300.0,
                                      date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Battery Replacement", cost=400.0,
                                      date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Transmission Repair", cost=500.0,
                                      date=datetime.datetime.now())
        models.Service.objects.create(vehicle=self.vehicle, description="Engine Overhaul", cost=600.0,
                                      date=datetime.datetime.now())


    def test_total_cost(self):
        response = self.client.get(f'/vehicles/{self.vehicle.id}/total_service_cost/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('total_cost'), 2100.0)



