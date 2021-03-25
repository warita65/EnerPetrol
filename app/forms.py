from django import forms
from app.models import FeedbackContacts


class FeedbackContactsForm(forms.ModelForm):
    
    class Meta:
        model = FeedbackContacts
        fields = ('full_name', 'email', 'phone_number', 'subject', 'message',)