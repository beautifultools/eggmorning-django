from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['get'])
def fetch_user(request):
	#fetch all user objects
    users = User.objects.all()
    serializer = UserSerializer(users, context = {'request' : request}, many = True)
    
    #return Response using rest_framework's response
    return Response(serializer.data)


