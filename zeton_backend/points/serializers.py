from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.Serializer):
    class Meta:
        model = Point
        fields = ['id', 'origin', 'value']

    def create(self, validated_data):
        """
        Create and return a new `Point` instance, given the validated data.
        """
        return Point.objects.create(**validated_data)
