from django.db import models


class BookId(models.Model):
    book_id = models.CharField(
        max_length=100,
        blank=True,
        null=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReadCsv(models.Model):
    book = models.ForeignKey(
        BookId,
        on_delete=models.CASCADE,
        to_field='book_id',
        blank=True,
        null=False,
        default=0,
    )

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
