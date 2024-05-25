from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView

router = DefaultRouter()
# router.register(r'providers', ProviderViewSet)
# router.register(r'appointments', AppointmentViewSet)
# router.register(r'reviews', ReviewViewSet)
# router.register(r'resources', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),  # Add this line for the RegisterView
]
