from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common_utils.utils import validate_jwt
from authentication.serializer import UserSerializer
from authentication.models import User
from common_utils.utils import generate_jwt

class Login(APIView):
    # /login | {email:"", password:""}
    def post(self, request, format=None):
        email=request.data.get("email")
        password=request.data.get("password")
        print(email , password)
        
        try:
            user_obj=User.objects.get(email=email,password=password)
        except Exception as e:
            return Response({"message":"login failed"},status=401)  
        else:
            u=generate_jwt(user_obj)
            return Response({"message":"login successful","token":u},status=200)      
        print(user_obj)

        return Response({})

class Logout(APIView):
    def get(self, request, format=None):
        print("this is GET")
        
        return Response({})

    def post(self, request, format=None):
        print("this is post")
        return Response({})
    