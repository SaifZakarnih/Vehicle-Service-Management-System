from django.db import models
import datetime
# Create your models here.


class Vehicle(models.Model):
    vin = models.CharField(max_length=17)  # After looking this up, it seems it's made of 17 characters?
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    year = models.IntegerField()

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.make + ' - ' + str(self.model) + ' - ' + str(self.year)


class Service(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.FloatField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.vehicle.make + ' - ' + str(self.date.year)


class Mechanic(models.Model):
    name = models.CharField(max_length=32)
    specialization = models.CharField(max_length=32)
    services = models.ManyToManyField(Service)

    class Meta:
        verbose_name = 'Mechanic'
        verbose_name_plural = 'Mechanics'

    def __str__(self):
        return self.name + ' - ' + self.specialization


class Lead(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    vehicles = models.ManyToManyField(Vehicle)

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ContactInformation(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=20)
    contact_value = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contacts Information'

    def __str__(self):
        return self.lead.first_name + self.lead.last_name + ' - ' + self.contact_value


