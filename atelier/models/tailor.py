from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from atelier.models import Atelier
from atelier.models.abstract_base import AbstractBaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Tailor(AbstractBaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    atelier = models.ForeignKey(
        Atelier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('atelier')
    )

    # email_confirmed = models.BooleanField(
    #     default=False
    # )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Tailor.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.tailor.save()

    def __str__(self):
        """
        to display an object in the Django admin site
        and as the value inserted into a template when it displays an object
        """
        return self.user

    class Meta:
        ordering = ['user']

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('atelier:tailor_detail', args=[str(self.id)])
