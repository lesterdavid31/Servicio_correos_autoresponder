from django import forms
from .models import NewsLettersUser, NewsLetter

class NewsletterUserSgnupForm(forms.ModelForm):
    class Meta:
        model = NewsLettersUser
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].error_messages = {
            'unique': "Este correo ya está registrado. Por favor usa otra dirección"
        }

class NewsLetterCreationForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['name','subject','body','email','status']

