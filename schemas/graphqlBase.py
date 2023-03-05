import strawberry
from strawberry.fastapi import GraphQLRouter
from .mutateSchema import *
from .querySchema import *


schema = strawberry.Schema(query=Query,mutation=Mutation)
graphql_app = GraphQLRouter(schema)