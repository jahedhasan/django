from django import forms
from .models import StudentFeedback



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your feedback'}),
        }
