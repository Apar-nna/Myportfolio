# profiles/forms.py

from django import forms
from .models import Profile, PortfolioItem

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'skills', 'contact']

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['title', 'description', 'image', 'link', 'project_description', 'project_image', 'project_link']
