import graphene
from .models import Book, Author


class BookType(graphene.ObjectType):
    class Meta:
        model = Book


class AuthorType(graphene.ObjectType):
    class Meta:
        model = Author

