from django import forms
from .models import Book, BookSize, Author


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "price", "book_size_id")


class CreateNewBookForm(forms.Form):
    title = forms.CharField(required=True)
    price = forms.IntegerField(required=True)
    book_price_id = forms.ModelChoiceField(BookSize.objects, required=True)

    def save(self):
        return Book.objects.create(
            title=self.cleaned_data["title"],
            price=self.cleaned_data["price"],
            book_id=self.cleaned_data["book_id"],
        )


