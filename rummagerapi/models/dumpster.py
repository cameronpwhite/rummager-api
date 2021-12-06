from django.db import models

class Dumpster(models.Model):

    location = models.CharField(max_length=50)