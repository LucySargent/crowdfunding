from .permissions import IsOwnerOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.http import Http404
from rest_framework import status


# Create your views here.
class CustomUserList(APIView):
# GET method - retrieve all users
    def get(self, request):
        if self.request.user.is_superuser:
            customuser = CustomUser.objects.all()
        else:
            customuser = CustomUser.objects.filter(username=self.request.user)

        serializer = CustomUserSerializer(customuser, many=True) #explicity stating the relationship
        return Response(serializer.data)

# POST method - create a new user
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# /users/<pk>
class CustomUserDetail(APIView):
    permission_classes = [
        IsOwnerOrReadOnly
    ]
# helper method for getting a user and raising a 404 if that user does not exist
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

# GET a single user's detail    
         
    def get(self, request, pk):
        user = self.get_object(pk)
        if request.user != user:
            return Response({"message":"no"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
        

#new code for updating user details - name,email   
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance=user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "User deleted"})

    