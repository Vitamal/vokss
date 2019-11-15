from django.contrib.auth import get_user_model
from django.db import models


class AbstractBaseModel(models.Model):

    created_datetime = models.DateTimeField(
        auto_now_add=True
    )

    last_updated_datetime = models.DateTimeField(
        auto_now=True
    )

    created_by = models.ForeignKey(
        get_user_model(), null=True, blank=True, related_name='+'
    )

    last_updated_by = models.ForeignKey(
        get_user_model(), null=True, blank=True, related_name='+'
    )

    class Meta:
        abstract = True
