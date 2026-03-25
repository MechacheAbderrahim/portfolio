from rest_framework import viewsets
from .models import PortfolioItem
from .serializers import PortfolioItemSerializer

class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer