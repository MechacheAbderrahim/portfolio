from rest_framework import viewsets
from .models import PortfolioItem, UserProfile, Skill, Technology
from .serializers import PortfolioItemSerializer, UserProfileSerializer, SkillSerializer, TechnologySerializer


class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all().select_related('user').prefetch_related('skills', 'technologies')
    serializer_class = PortfolioItemSerializer
    lookup_field = 'slug'


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer