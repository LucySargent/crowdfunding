from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SUB_CHOICES, Beefriend, Project, Pledge
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer, PledgeDetailSerializer, BeefriendSerializer, BeefriendDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view

# for /projects
class ProjectList(APIView):
    # this make it so that a user must be logged in to post a project (iow removes the post button from /projects list)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# for GET /projects
    def get(self, request):
        #get all the projects
        projects = Project.objects.all()
        #serialize all the projects
        serializer = ProjectSerializer(projects, many=True)
        #send all the serialized projects back in response body
        return Response(serializer.data)

# for POST /projects/
    def post(self, request):
         # try to create a serializer from the data in the request body
        serializer = ProjectSerializer(data=request.data)
        # if the serializer thinks it's valid
        if serializer.is_valid():
            # save the object
            serializer.save(owner=request.user)
            # send the serialized (saved) data back in response body
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# for /projects/<pk>
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
# helper method to get the object with the pk    
    # for GET /projects/<pk>
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
            # return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

# update /project/<pk>
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

# delete project
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(dict(message= 'Project deleted!'))


# for /pledges/
class PledgeList(APIView):

# GET /pledges/
    def get(self, request):
            pledges = Pledge.objects.all()
            serializer = PledgeSerializer(pledges, many=True)
            return Response(serializer.data)

# POST /pledges/
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# for /pledges/<pk>
class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
   
# for GET /pledges/<pk>
    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

# update /pledges/<pk>  
    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# delete /pledges/<pk>
    def delete(self, request, pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(dict(message= 'Pledge deleted!'))

# for /beefriends/
class BeefriendList(APIView):

    # GET /adoptions/
    def get(self, request):
            adopts = Beefriend.objects.all()
            serializer = BeefriendSerializer(adopts, many=True)
            return Response(serializer.data)

    # POST /beefriends/
    def post(self, request):
        serializer = BeefriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(beefriender=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
# for /beefriends/<pk>
class BeefriendDetail(APIView):

    def get_object(self, pk):
        try:
            beefriend = Beefriend.objects.get(pk=pk)
            self.check_object_permissions(self.request, beefriend)
            return beefriend
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        beefriend = self.get_object(pk)
        serializer = BeefriendSerializer(beefriend)
        return Response(serializer.data)

# update /beefriends/<pk>  
    def put(self, request, pk):
        beefriend = self.get_object(pk)
        data = request.data
        serializer = BeefriendDetailSerializer(
            instance=beefriend,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# delete /beefriends/<pk>
    def delete(self, request, pk):
        beefriend = self.get_object(pk)
        beefriend.delete()
        return Response(dict(message= 'You are no longer a Beefriend on this project.'))   

@api_view(['GET'])
def get_all_suburbs(request):
    suburbs = []
    for i in SUB_CHOICES:
        suburbs.append(i[0])
    return Response(suburbs)