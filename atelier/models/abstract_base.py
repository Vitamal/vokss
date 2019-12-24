from django.contrib.auth import get_user_model
from django.db import models


class AbstractBaseModel(models.Model):

    created_datetime = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    last_updated_datetime = models.DateTimeField(
        auto_now=True,
        null=True,
    )

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    last_updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    class Meta:
        abstract = True
