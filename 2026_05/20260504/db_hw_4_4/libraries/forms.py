from django import forms
from .models import Review
class LibrariesForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)
