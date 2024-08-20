from django.db import models
from django.contrib import admin
class Asset(models.Model):
    asset_type = models.CharField(max_length=100)
    asset_loc = models.CharField(max_length=100)
    thumbnail_loc = models.CharField(max_length=100)
    asset_desc = models.CharField(max_length=100)

admin.site.register(Asset)