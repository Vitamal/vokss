from django.db import models


class ComplicationElement(models.Model):
    name = models.CharField(max_length=264)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    allowed_fabric_complexity_group = models.ManyToManyField('atelier.FabricComplexityGroup')
    label = models.CharField(default='4', max_length=255)


    def __str__(self):
        return '{} {}'.format(self.label, self.name)