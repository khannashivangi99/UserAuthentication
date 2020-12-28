from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.models import User


class ResetPassword(APIView):
    # /resetpassword  
    def post(self, request, format=None):
        email=request.data.get("email")
        password=request.data.get("password")
        new_password=request.data.get("new_password")
        try:
            user_obj=User.objects.get(email=email,password=password)
            #print(user_obj.password)
        except Exception as e:
            print(e)
            return Response({"message":"incorrect credentials"},status=401)
        else:
            #override password
            user_obj.password=new_password
            user_obj.save() 
            #print(user_password)
            return Response({"message":"password reseted"},status=200)
        #print("this is post")
        return Response({}) 

class ForgetPassword(APIView):
    def get(self, request, format=None):
        print("this is GET")
        
        return Response({})

    def post(self, request, format=None):
        print("this is post")
        return Response({})