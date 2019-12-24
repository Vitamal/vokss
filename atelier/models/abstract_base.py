from django.contrib.auth import get_user_model
from django.db import models


class AbstractBaseModel(models.Model):
    """
    Abstract model to provide basic fields
    common for all models.

    """

    #: When was the instance created
    created_datetime = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    #: When was the instance last updated
    last_updated_datetime = models.DateTimeField(
        auto_now=True,
        null=True,
    )

    #: Who created the instance
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    #: Who was the last user to modify/update the instance
    last_updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    class Meta:
        abstract = True
