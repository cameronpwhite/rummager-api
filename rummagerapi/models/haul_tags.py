from django.db import models

class HaulTags(models.Model):

    haul = models.ForeignKey("Haul", on_delete=models.CASCADE)
    tags = models.ForeignKey("Tag", on_delete=models.CASCADE)