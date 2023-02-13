import graphene
from graphene_django import DjangoObjectType
from .models import Book, Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class Query:
    books = graphene.List(graphene.NonNull(BookType), description="書籍取得API")

    def resolve_books(self, info):
        return Book.objects.all()
