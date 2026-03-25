
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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



class ExpertiseView(APIView):
    def get(self, request):
        skills = Skill.objects.filter(display=True)
        technologies = Technology.objects.filter(display=True)
        languages = Language.objects.all()

        return Response({
            "research_areas": SkillSerializer(skills, many=True).data,
            "programming_tools": TechnologySerializer(technologies, many=True).data,
            "languages": LanguageSerializer(languages, many=True).data,
        })