from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectSerializer
from .models import Project

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of the rest api."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


    def perform_create(self, serializer):
        """Save the post data when creating a new project."""
        serializer.save()
