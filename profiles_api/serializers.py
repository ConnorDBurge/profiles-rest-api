from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out API view"""
    name = serializers.CharField(max_length=10) # post expects a 'name' to be passed