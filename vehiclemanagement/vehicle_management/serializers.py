from rest_framework import serializers
from . import models


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = '__all__'


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mechanic
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lead
        fields = '__all__'


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactInformation
        fields = '__all__'
