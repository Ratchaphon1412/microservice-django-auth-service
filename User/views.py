
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from Infrastructure.kafka.producer import sendData
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from Infrastructure.service import Facade


#Register API
class RegisterUserAPI(APIView):
    serializer_class = UserProfilesSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        token = Facade.securityService().generate_token(serializer.instance)
        data =  {
            "subject":"Email Verification",
            "template":"auth/email_verification.html",
            "to":[serializer.instance.email],
            "dataBinding":{
                "user":serializer.instance,
                "domain":"www.mininy.com",
                "uid":urlsafe_base64_encode(force_bytes(serializer.instance.pk)),
                "token":token,
            }
            
        }
        
        try:
            
            Facade.notificationService().send(data)
            
        except Exception as e:
            serializer.instance.delete()
            raise Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                "message": e,
            })
        
        
        return Response(
            status=status.HTTP_201_CREATED,
            data={"message":"Successfully Registered.",})
        
    
class UpdateUserAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfilesSerializer
    def put(self,request):
     
        
        serializers = self.serializer_class(request.user,data=request.data,partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                "message":"User Updated Successfully.",
            })
     
    

class DeleteUserAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfilesSerializer
    def delete(self,request):
        serializers = self.serializer_class(request.user)
        serializers.delete(request.user)
        return Response(
            status=status.HTTP_200_OK,
            data={
            "message":"User Deleted Successfully.",
        })

class GetUserAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfilesSerializer
    def get(self,request):
        serializers = self.serializer_class(request.user)
        
        return Response(
            status=status.HTTP_200_OK,
            data={
            "user":serializers.data,
            "message":"User Details.",
        })

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer


class ActivateUserAPI(APIView):
    def get(self,request,uidb64,token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            
            user = UserProfiles.objects.get(pk=uid)
        except Exception as e:
            user = None
            
            
        if user is not None and Facade.securityService().check_token(user,token):
            user.is_email_verified = True
            user.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                "message":"Email Verified Successfully.",
            })
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                "message":"Email Verification Failed.",
            })
            
class ReSendEmailVerify(APIView):
    serializer_class = ReSendEmailVerifySerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = UserProfiles.objects.filter(email=serializer.validated_data.get('email')).first()
            print(user)
            token = Facade.securityService().generate_token(user)
            data =  {
                "subject":"Email Verification",
                "template":"auth/email_verification.html",
                "to":[user.email],
                "dataBinding":{
                    "user":user,
                    "domain":"www.mininy.com",
                    "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                    "token":token,
                }
                
            }
            Facade.notificationService().send(data)
            
        
        return Response(
            status=status.HTTP_200_OK,
            data={
            "message":"Email Verification Link Sent Successfully.",
        })

class AddressAPI(APIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(
            status=status.HTTP_201_CREATED,
            data={
            "message":"Address Added Successfully.",
        })
        
    def get(self,request):
        user = request.user
        address = user.address_set.all()
        return Response(
            status=status.HTTP_200_OK,
            data={
            "address":AddressSerializer(address,many=True).data,
            
        })
        
    def put(self,request):
        address = request.user.address_set.filter(address_id=request.data.get('address_id')).first()
        serializer = self.serializer_class(address,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(address,serializer.validated_data)
        return Response(
            status=status.HTTP_200_OK,
            data={
            "message":"Address Updated Successfully.",
        })
    
    
    
    def delete(self,request):
        user = request.user
        address = user.address_set.filter(address_id=request.data.get('address_id')).first()
        address.delete()
        return Response(
            status=status.HTTP_200_OK,
            data={
            "message":"Address Deleted Successfully.",
        })
        
        
        
class AddressViewAPI(APIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        user = request.user
        address = user.address_set.filter(address_id=pk).first()
        return Response(
            status=status.HTTP_200_OK,
            data={
            "address":AddressSerializer(address).data,
            
        })

class InfrastructureUserAPI(APIView):
    def post(self,request):
        user = UserProfiles.objects.get(pk=request.data.get('user_id'))
        return Response(
            status=status.HTTP_200_OK,
            data={
            "user":UserProfilesSerializer(user).data,
        })
    
    
    
# class ListAllUsersAPI(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserProfilesSerializer
#     def get(self,request):
#         users = UserProfiles.objects.all()
#         serializers = self.get_serializer(users,many=True)
#         return Response(
#             status=status.HTTP_200_OK,
#             data={
#             "users":serializers.data,
#             "message":"List of all users.",
#         })