from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Profile, Skill, Project, Experience, Contact
from .serializers import ProfileSerializer, SkillSerializer, ProjectSerializer, ExperienceSerializer, ContactSerializer

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=['get'])
    def main(self, request):
        profile = self.queryset.first()
        if profile:
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        return Response({'detail': 'Nenhum perfil encontrado'}, status=status.HTTP_404_NOT_FOUND)

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        skills = self.queryset.all()
        categories = {}

        for skill in skills:
            if skill.category not in categories:
                categories[skill.category] = []
            categories[skill.category].append(SkillSerializer(skill).data)
        
        return Response(categories)

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_projects = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)
