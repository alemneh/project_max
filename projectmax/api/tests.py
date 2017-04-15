from django.test import TestCase
from .models import Project
from rest_framework.test import APIClient
from rest_framework import status_code
from django.core.urlresolvers import reverse
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the buketlist model"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.project_name = "Going Green"
        self.project = Project(name=self.project_name)
        # self.project_length = "4 Weeks"
        # self.project_description = "Provide a map for recycling centers in Seattle."
        # self.project_manager = "Alem Asefa"

    def test_model_can_create_a_bucketlist(self):
        """Test the project model can create a project."""
        old_count = Project.objects.count()
        self.project.save()
        new_count = Project.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for api views"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.response = self.client.post(
            reverse('create'),
            self.project_data,
            format="json")

    def test_api_can_create_a_project(self):
        """Test the api has project creation capability."""
        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_project(self):
        """Test the api can get given project."""
        project = Project.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': project.id}, format="json")

    def test_api_can_update_project(self):
        """Test the api can update a given project"""
        change_project = {'name': 'Star hunters'}
        res = self.client.put(
            reverse('details', kwargs={'pk': project.id}),
            change_project, format='json')
        self.assertEquals(res.status_code, status.HTTP_201_OK)

    def test_api_can_delete_project(self):
        """Test the api can delete a given project"""
        project = Project.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': project.id}),
            format='json',
            follow=True)
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
