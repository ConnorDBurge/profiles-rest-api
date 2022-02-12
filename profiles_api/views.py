from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer


class HelloApiView(APIView):
    """Test API View"""
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