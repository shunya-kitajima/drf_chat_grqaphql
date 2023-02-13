import graphene
from .models import Book, Author


class BookType(graphene.ObjectType):
    class Meta:
        model = Book


class AuthorType(graphene.ObjectType):
    class Meta:
        model = Author


class Query:
    books = graphene.List(graphene.NonNull(BookType), description="書籍取得API")

    def resolve_books(self, info):
        return Book.objects.all()
