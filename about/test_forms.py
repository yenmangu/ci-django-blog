from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields"""
        form = CollaborateForm(
            {
                "name": "test",
                "email": "test@test.com",
                "message": "test-messages",
            }
        )
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_not_valid_if_field_empty(self):
        """Test a single field"""
        form = CollaborateForm(
            {
                "name": "",
                "email": "",
                "message": "",
            }
        )
        self.assertFalse(
            form.is_valid(), msg="Fields were not provided, but the form is valid"
        )

    def test_name_is_required(self):
        """Test name field"""
        form = CollaborateForm(
            {
                "name": "",
                "email": "email@email.com",
                "message": "Test message",
            }
        )

        self.assertFalse(
            form.is_valid(), msg="Name was not provided but the form is valid"
        )

    def test_email_is_required(self):
        """Test email field"""
        form = CollaborateForm(
            {
                "name": "First Second",
                "email": "email@email.com",
                "message": "teeeeessssrrrrrrrr",
            },
        )
