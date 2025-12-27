from django.test import TestCase
from .forms import CommentForm

# Create your tests here.


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        """Test that the form is valid with a non-empty body."""
        comment_form = CommentForm({"body": "This is a great post!"})
        self.assertTrue(
            comment_form.is_valid(),
            msg="The form should be valid when the body...§/ has content.",
        )

    def test_form_is_invalid_if_body_is_empty(self):
        """Test that the form is invalid if the body is empty."""
        comment_form = CommentForm({"body": ""})
        self.assertFalse(
            comment_form.is_valid(), msg="Form should be invalid with an empty body"
        )
