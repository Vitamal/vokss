from django.contrib.auth import get_user_model
from django.db import models

from atelier.models.abstract_base import AbstractBaseModel


class Atelier(AbstractBaseModel):
    name = models.CharField(
        max_length=150,
    )

    tailor = models.ManyToManyField(
        get_user_model(),
    )
