from django import forms
from app.models import FeedbackContact

class FeedbackContactForm(forms.ModelForm):    
    class Meta:
        model = FeedbackContact
        fields = ('full_name', 'email', 'phone_number', 'subject', 'message',)