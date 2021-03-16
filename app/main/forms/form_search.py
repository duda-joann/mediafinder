from django import forms
from main.models import Search


class FormSearch(forms.ModelForm):

    """Form to get from user  search word"""

    class Meta:
        model = Search
        fields = ('search_word', 'filter')
