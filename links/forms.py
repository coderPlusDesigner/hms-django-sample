from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title', 'url', 'description', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Awesome Django Resource'}),
            'url': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What is this link about?'}),
        }