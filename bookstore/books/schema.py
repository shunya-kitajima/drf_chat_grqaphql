import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from .models import Book, Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = {
            "title": ["exact", "icontains"],
        }

    interfaces = (relay.Node,)


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class Query:
    books = graphene.List(graphene.NonNull(BookType), description="書籍取得API")

    def resolve_books(self, info):
        return Book.objects.all()
