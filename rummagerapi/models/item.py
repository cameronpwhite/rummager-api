from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Items(models.Model):

    name = CharField(max_length=50)
    haul_id = models.ForeignKey(Haul, on_delete=models.CASCADE)