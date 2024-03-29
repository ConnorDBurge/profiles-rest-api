from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated 


from .serializers import HelloSerializer
from .serializers import UserProfileSerializer
from .serializers import ProfileFeedItemSerializer
from .permissions import UpdateOwnProfile, UpdateOwnStatus
from .models import UserProfile, ProfileFeedItem


class HelloApiView(APIView):
    """Test API View"""
    """For an APIView, you add methods that match the type of HTTP request"""
    serializer_class = HelloSerializer

    # api/hello-view/
    def get(self, request, format=None): 
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, path, put, delete)',
            'Is similar to traditional Django view',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    # api/hello-view/
    def post(self, request):
        """Create a hellow message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # api/hello-view/
    def put(self, request, pk=None):
        """Handle complete updating an object"""
        return Response({'method': 'PUT'})
    
    # api/hello-view/
    def patch(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PATCH'})
    
    # api/hello-view/
    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""
    """For an API View Set, you add methods that are actions"""
    serializer_class = HelloSerializer

    # api/hello-viewset/
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})
    
    # api/hello-viewset/
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # api/hello-viewset/:pk
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'method': 'GET'})
    
    # api/hello-viewset/:pk
    def update(self, request, pk=None):
        """Handle updating an object by its id"""
        return Response({'method': 'PUT'})

    # api/hello-viewset/:pk
    def partial_update(self, request, pk=None):
        """Handle updating part of an object by its id"""
        return Response({'method': 'PATCH'})

    # api/hello-viewset/:pk
    def destroy(self, request, pk=None):
        """Handle deleting an object by its id"""
        return Response({'method': 'DELETE'})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    # api/profile/ (GET, POST)
    # api/profile/:id (GET, POST, PUT, PATCH, DELETE)
    # api/profile/?search=<TERM>
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # tuple
    permission_classes = (UpdateOwnProfile,) # tuple
    filter_backends = (filters.SearchFilter,) # tuple
    search_fields = ('name', 'email',) # tuple
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user profile feed items"""
    serializer_class = ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,) # tuple
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnStatus, IsAuthenticated,) # tuple
    
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)