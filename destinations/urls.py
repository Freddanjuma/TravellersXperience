from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet, destinations_list

router = DefaultRouter()
router.register(r'', DestinationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),         # REST API endpoints
    path('', destinations_list, name='destinations-page'),  # HTML page
]

