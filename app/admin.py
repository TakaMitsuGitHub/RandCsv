from django.contrib import admin

from . import models

admin.site.register(models.CreateCsv)
admin.site.register(models.ReadCsv)
