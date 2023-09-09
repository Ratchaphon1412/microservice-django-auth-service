from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from Infrastructure.kafka.producer import sendData




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


class TestSendTOKafka(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        
        
        response_kafka = sendData("test",str({'data':'test','data2':'test2'}))
        print (response_kafka)
        return Response({
            "message":response_kafka
        })
