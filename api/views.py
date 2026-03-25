from rest_framework import viewsets
from .models import PortfolioItem, UserProfile
from .serializers import PortfolioItemSerializer, UserProfileSerializer


class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer