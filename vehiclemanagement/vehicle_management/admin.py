from django.contrib import admin
from . import models

admin.site.register(models.Vehicle)

admin.site.register(models.Service)

admin.site.register(models.Mechanic)

admin.site.register(models.Lead)

admin.site.register(models.ContactInformation)