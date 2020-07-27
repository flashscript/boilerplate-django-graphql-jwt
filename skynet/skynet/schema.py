from user.schema import Query, Mutation
import graphene
import graphql_jwt

class Query(Query, graphene.ObjectType):
  # This class will inherit from multiple Queries
  # as we begin to add more apps to our project
  pass

class Mutation(Mutation, graphene.ObjectType):
	login = graphql_jwt.ObtainJSONWebToken.Field()
	verify = graphql_jwt.Verify.Field()
	refresh = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)