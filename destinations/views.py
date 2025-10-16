from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def destinations_list(request):
    return render(request, 'users/HTMLs/destinations.html')
