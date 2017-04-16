from django.test import TestCase
from .models import Project
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the buketlist model"""

    def setUp(self):
        """Define the test client and other test variables"""
        user = User.objects.create(username="nerd")
        self.project_name = "Going Green"
        # specify owner of project
        self.project = Project(name=self.project_name, owner=user)


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
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.project_data = {'name': 'New Way Out', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.project_data,
            format="json")

    def test_api_can_create_a_project(self):
        """Test the api has project creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/projects/', kwargs={'pk': 3}, format='json')
        print (res.status_code)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_project(self):
        """Test the api can get given project."""
        project = Project.objects.get(id=1)
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': project.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, project)

    def test_api_can_update_project(self):
        """Test the api can update a given project"""
        change_project = {'name': 'Star hunters'}
        project = Project.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': project.id}),
            change_project, format='json')
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_project(self):
        """Test the api can delete a given project"""
        project = Project.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': project.id}),
            format='json',
            follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
