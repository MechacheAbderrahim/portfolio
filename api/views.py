from rest_framework import viewsets
from .models import PortfolioItem, UserProfile, Skill, Technology, Education, Language, Publication
from .serializers import PortfolioItemSerializer, UserProfileSerializer, SkillSerializer, TechnologySerializer, EducationSerializer, LanguageSerializer, PublicationSerializer

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


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().select_related('user')
    serializer_class = EducationSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().select_related('user')
    serializer_class = LanguageSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all().select_related('user')
    serializer_class = PublicationSerializer