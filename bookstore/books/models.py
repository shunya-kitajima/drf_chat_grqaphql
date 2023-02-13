from django.db import models
import uuid


class BookSize(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30, blank=False)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=30, blank=False)
    price = models.IntegerField(default=0)
    book_size_id = models.ForeignKey(
        BookSize,
        related_name="book_size_id",
    )


class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    middle_name = models.CharField(max_length=30, blank=True)


class BookAuthor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    book_id = models.ForeignKey(
        Book,
        related_name="book_id",
        on_delete=models.CASCADE,
    )
    author_id = models.ForeignKey(
        Author,
        related_name="author_id",
        on_delete=models.CASCADE,
    )
