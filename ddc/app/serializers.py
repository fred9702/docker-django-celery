from rest_framework import serializers

from app.models import Dog


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = (
            'name',
            'age',
            'breed'
        )