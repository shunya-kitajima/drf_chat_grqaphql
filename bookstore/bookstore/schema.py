import graphene
import bookstore.books.schema


class Query(bookstore.books.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
