from django.shortcuts import render

# Create your views here.


class HitViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = HitSerializer
    queryset = Hit.objects.all()
