from django.db import models

class AllowanceDiscount(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.DecimalField(max_digits=5, decimal_places=2)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.name
