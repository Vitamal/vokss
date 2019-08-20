from django.db import models


class Fabric(models.Model):
    name = models.CharField(max_length=264)
    group = models.ForeignKey('atelier.FabricComplexityGroup', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name