from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    origin = forms.CharField(label='Origin_book_evolved')
    class Meta:
        model = Book
        fields = ['title', 'origin', 'description', 'author']
