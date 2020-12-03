from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common_utils.utils import validate_jwt

class Login(APIView):
    
    @validate_jwt
    def get(self, request):
        print("this is GET")
        print(request.META["HTTP_AUTHORIZATION"])
        
        return Response({})

    def post(self, request, format=None):
        print("this is post")
        return Response({})

class Logout(APIView):
    def get(self, request, format=None):
        print("this is GET")
        
        return Response({})

    def post(self, request, format=None):
        print("this is post")
        return Response({})
    