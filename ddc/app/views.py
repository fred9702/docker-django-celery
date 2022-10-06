from django.conf import settings

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.serializers import DogSerializer
from app.models import Dog


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    # permission_classes = [IsAuthenticated]
    basename = "dog"

    def get_queryset(self):
        return super(DogViewSet, self).get_queryset()

    def list(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        data = DogSerializer(query_set, many=True).data
        return Response(data={'error': False, 'message': None, 'results': data})

    def create(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        request_data = request.data
        dog, created = Dog.objects.get_or_create(
            name=request_data['name'], 
            age=request_data['age'], 
        )
        data = DogSerializer(dog).data
        return Response(data={'error': False, 'message': "Dog object successfully created", 'results': data})
