from django.db import models
from dstorage_ccapudev import storage

# Create your models here.
class Banners(models.Model):
    img = models.FileField(storage=storage.CustomStorage)