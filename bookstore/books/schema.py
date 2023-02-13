import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from .models import Book, Author
from .forms import CreateBookForm


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
    full_name = graphene.String()

    def resolve_authors(self: Author, info):
        return f"{self.last_name} {self.first_name}"


class Query:
    books = graphene.List(
        graphene.NonNull(BookType),
        title=graphene.String(required=False),
        description="書籍取得API",
    )

    def resolve_books(self, info, title: str = ""):
        qs = Book.objects.all()
        if title:
            qs = qs.filter(title__contains=title)
        return qs


class CreateBookMutation(DjangoModelFormMutation):
    class Meta:
        form_class = CreateBookForm


class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
