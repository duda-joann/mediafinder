from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from main.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('review', 'rate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('review', css_class="form-group col-md-12"),
                Column('rate', css_class="form-group col-md-12"),
            ),
            Submit('submit', 'Submit',  css_default='btn_default'))

