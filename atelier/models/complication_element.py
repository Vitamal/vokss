from django.db import models


class ComplicationElement(models.Model):
    name = models.CharField(max_length=264)
    base_price = models.IntegerField(default=0)
    allowed_materials = models.ManyToManyField('atelier.Fabric')

    def __str__(self):
        return self.name