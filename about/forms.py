from .models import CollaborationRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborationRequest
        fields = (
            "name",
            "email",
            "message",
        )
