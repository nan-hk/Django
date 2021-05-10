from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publisher', 'summary', 'releaseDate', 'category')
        widgets = {
                'releaseDate': forms.SelectDateWidget(),
            }
