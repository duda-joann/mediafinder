from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Search, Rating
from .validators import validate_age


class FormSearch(forms.ModelForm):

    """Form to get from user  search word"""


    class Meta:
        model = Search
        fields = ('search_word', 'filter')


class RegisterForm(UserCreationForm):

    """Registration form for new user"""

    name = forms.CharField(max_length=100,
                           validators=[RegexValidator(regex='^[a-zA-Z]$',
                                                      message='This in not name',
                                                      )]
                           )
    email = forms.EmailField(max_length=100)
    date_of_birth = forms.DateTimeField(validators=[validate_age])

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6  mb-0'),
                Column('name', css_class='form-group col-md-6  mb-0'),
                css_class='form-row'),
            'email',
            Row(
                Column('password1', css_class='form-group col-md-4  mb-0'),
                Column('password2', css_class='form-group col-md-4  mb-0'),
                Column('date_of_birth', css_class='forms-group col md-4 mb=0'),
                css_class='form-row'
            ),

            Submit('submit', 'Sign in')
        )


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
