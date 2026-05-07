from django import forms
from .models import Book, Author

class CommentForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'adult', 'price', )