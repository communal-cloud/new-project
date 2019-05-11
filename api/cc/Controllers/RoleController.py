import logging

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cc.Services.RoleService import RoleService


class RoleController(APIView):
	__logger = logging.getLogger('RoleController')
	__roleService = RoleService.Instance()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
