from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "price", "book_size_id")
