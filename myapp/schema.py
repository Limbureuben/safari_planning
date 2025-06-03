import graphene
from .views import *

class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, world!")

schema = graphene.Schema(query=Query, mutation=Mutation)