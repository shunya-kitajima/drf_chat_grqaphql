import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from .models import Book, Author
from .forms import CreateBookForm, CreateNewBookForm


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
    full_name = graphene.String()

    def resolve_authors(self: Author, info):
        return f"{self.last_name} {self.first_name}"


class NewBookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    price = graphene.Int(required=True)
    book_size_id = graphene.UUID(required=True)
    author_id = graphene.UUID(required=True)


class CreateBookMutation(graphene.Mutation):
    class Meta:
        output = BookType

    class Arguments:
        new_book_input = NewBookInput(required=True)

    def mutate(self, info, new_book_input: NewBookInput):
        form = CreateNewBookForm(data=new_book_input)
        if form.is_valid():
            book = form.save()
            return book


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


class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
