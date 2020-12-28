from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common_utils.utils import validate_jwt
from authentication.serializer import UserSerializer
from authentication.models import User
import json
from django.forms.models import model_to_dict

class Signup(APIView):

    @validate_jwt
    def get(self, request):
        user_id=request.query_params.get("user_id")
        query_set=User.objects.get(id=user_id)
        dict_obj = model_to_dict( query_set)
        return Response(dict_obj)

    def post(self, request, format=None):
        serializer = UserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    