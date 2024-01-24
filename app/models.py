from django.db import models


class CreateCsv(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    rank = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReadCsv(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    rank = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

