from rummagerapi.models.haul import Haul
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Item(models.Model):

    name = CharField(max_length=50)
    haul = models.ForeignKey("Haul", on_delete=models.CASCADE, related_name="items")