from django import forms
from .models import Review

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'star_point']

class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']