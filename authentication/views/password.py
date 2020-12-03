from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ResetPassword(APIView):
    def get(self, request, format=None):
        print("this is GET")
        
        return Response({})

    def post(self, request, format=None):
        print("this is post")
        return Response({})

class ForgetPassword(APIView):
    def get(self, request, format=None):
        print("this is GET")
        
        return Response({})

    def post(self, request, format=None):
        print("this is post")
        return Response({})