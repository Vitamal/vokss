from django.db import models

class MyClient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tel_number = models.IntegerField(blank=True)
    place = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('client-detail', args=[str(self.id)])
