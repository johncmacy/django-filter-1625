from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    pass


class Publisher(models.Model):
    name = models.CharField(max_length=25)


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="books",
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name="books",
    )
