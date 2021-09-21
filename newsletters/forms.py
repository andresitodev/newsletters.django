from django import forms
from .models import NewsletterUser


class NewsletterUserSignupForm(forms.ModelForm):
    class Meta:
        models = NewsletterUser
        fields = ['email']


class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        models = Newsletter
        fields = ['name', 'subject', 'body', 'email']