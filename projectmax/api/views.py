from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsOwner
from django.contrib.auth.models import User
from .serializers import ProjectSerializer
from .models import Project

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of the rest api."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)


    def perform_create(self, serializer):
        """Save the post data when creating a new project."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the GET, PUT, and requests."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)
