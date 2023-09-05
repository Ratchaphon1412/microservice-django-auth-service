from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer


#Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "user":UserSerializer(serializer.instance).data,
                "message":"User Created Successfully.  Now perform Login to get your token",
            })
        else:
            return Response({
                "user":serializer.errors,
                "message":"User Creation Failed",
            })


# Create your views here.
