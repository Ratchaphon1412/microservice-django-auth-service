
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from Infrastructure.kafka.producer import sendData




#Register API
class RegisterUserAPI(APIView):
    serializer_class = UserProfilesSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
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
            "user":UserProfilesSerializer(serializers.instance).data,
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