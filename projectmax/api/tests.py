from django.test import TestCase
from .models import Project
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
