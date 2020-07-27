from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
import graphene
import graphql_jwt

class UserType(DjangoObjectType):
	class Meta:
		model = get_user_model()

class Query(object):
	users = graphene.List(UserType)

	@login_required
	def resolve_users(self, info, **kwargs):
		return get_user_model().objects.all()