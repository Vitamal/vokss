from django.db import models


class ComplicationElement(models.Model):
    name = models.CharField(max_length=264)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    allowed_materials = models.ManyToManyField('atelier.Fabric')

    def __str__(self):
        return self.name