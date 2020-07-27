from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
import graphene
import graphql_jwt

class UserType(DjangoObjectType):
	class Meta:
		model = get_user_model()
		fields = ('id', 'username', 'email',)

class SignUp(graphene.Mutation):
  user = graphene.Field(UserType)
  
  class Arguments:
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)

  def mutate(self, info, username, password, email):
    user = get_user_model()(
        username=username,
        email=email,
    )
    user.set_password(password)
    user.save()

    return SignUp(user=user)

class Query(object):
	users = graphene.List(UserType)
	me = graphene.Field(UserType)

	@login_required
	def resolve_users(self, info, **kwargs):
		if info.context.user.is_superuser:
			return get_user_model().objects.all()
		elif info.context.user.is_staff:
			return get_user_model().objects.all()
		else:
			return Exception('Unauthorized')

	@login_required
	def resolve_me(self, info, **kwargs):
		return info.context.user

class Mutation(graphene.ObjectType):
  singup = SignUp.Field()  