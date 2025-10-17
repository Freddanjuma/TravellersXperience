from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer
from django.shortcuts import render

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all().order_by('-created_at')
    serializer_class = DestinationSerializer

# template view to render your destinations.html
def destinations_list(request):
    return render(request, 'users/HTMLs/destinations.html')

def ratetracker_view(request):
    return render(request, 'users/HTMLs/ratetracker.html')