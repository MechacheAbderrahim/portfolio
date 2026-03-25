from rest_framework import serializers
from .models import (
    PortfolioItem,
    Technology,
    Skill,
    UserProfile,
    Education,
    Language,
    Publication,
)


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name', 'category', 'icon_url']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'full_name', 'title', 'subtitle', 'email', 'location']


class PortfolioItemSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = PortfolioItem
        fields = [
            'id',
            'title',
            'slug',
            'subtitle',
            'organization',
            'description',
            'type',
            'employment_type',
            'location',
            'start_date',
            'end_date',
            'is_current',
            'image_url',
            'project_url',
            'highlight',
            'order_index',
            'user',
            'technologies',
            'skills',
            'created_at',
            'updated_at',
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'