from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'goal', 'notes']
        widgets = {
            'goal': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Example validation: enforce company domain (optional). Comment out if not needed.
        # if not email.endswith('@example.com'):
        #     raise forms.ValidationError('Please use your company email.')
        return email
