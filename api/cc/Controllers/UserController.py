import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from cc.Services.UserService import UserService
from cc.Serializers.UserSerializer import UserSerializer
from cc.Serializers.RegisterSerializer import RegisterSerializer
from cc.CustomPermissions import IsPostOrIsAuthenticated
from cc.models import User, ActivationToken
import json

class UserAPIViewController(APIView):
	__logger = logging.getLogger('UserController')
	__userService = UserService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsPostOrIsAuthenticated,)

	def get(self, request, format=None):
		user = request.user
		userJson = UserSerializer(user)
		return Response(userJson.data)

	def post(self, request, format=None):
		requestDataParsed = json.loads(request.body)
		user = self.__userService.Register(requestDataParsed)
		userSerialized = UserSerializer(user)
		return Response(userSerialized.data)
	
	def put(self, request, format=None):
		requestDataParsed = json.loads(request.body)
		user = self.__userService.UpdateUser(request.user, requestDataParsed.data)
		userSerialized = UserSerializer(user)
		return Response(userSerialized.data)
	
	def delete(self, request, format=None):
		requestDataParsed = json.loads(request.body)
		return self.__userService.DeleteUser(requestDataParsed.user)

class UserViewSetController(ViewSet):
	__logger = logging.getLogger('UserController')
	__userService = UserService.Instance()

	@action(detail=True, methods=['post'])
	def activation(self, request, pk=None):
		token = request.query_params['token']
		return self.__userService.ActivateEmail(token)

	@action(detail=True, methods=['post'])
	def forgot_password(self, request, pk=None):
		requestDataParsed = json.loads(request.body)
		email = requestDataParsed['email']
		baseUrl = request.build_absolute_uri()
		return self.__userService.ForgotPassword(email, baseUrl)

	@action(detail=True, methods=['get'], permission_classes=[IsAuthenticated], authentication_classes=[TokenAuthentication])
	def logout(self, request, pk=None):
		return self.__userService.Logout(request.user)