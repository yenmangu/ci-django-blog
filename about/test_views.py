from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .views import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        """Set up mock About context"""
        self.user = User.objects.create_superuser(
            username="myUsername", email="test@test.com", password="myPassword"
        )
        self.about = About(
            title="Test about",
            content="About content",
        )
        self.about.save()

    def test_about_loads_with_form(self):
        """Verfifies GET requerst for about me containing collaboration form"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test about", response.content)
        # print(response.context)
        self.assertIsInstance(response.context["collaborate_form"], CollaborateForm)

    def test_successfull_collaboration_request_submission(self):
        """Verfies POST request for collaboration request"""
        # self.client.login(username="myUsername", password="myPassword")
        post_data = {
            "name": "test name",
            "email": "test@test.com",
            "message": "test message",
        }
        response = self.client.post(reverse("about"), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content,
        )
