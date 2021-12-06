from rummagerapi.models.tag import Tag
from rummagerapi.models.dumpster import Dumpster
from rummagerapi.models.diver import Diver
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

class Haul(models.Model):

    description = CharField(max_length=50)
    image_path = models.ImageField(upload_to='images/')
    diver_id = models.ForeignKey(Diver, on_delete=models.CASCADE)
    dumpster_id = models.ForeignKey(Dumpster, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)