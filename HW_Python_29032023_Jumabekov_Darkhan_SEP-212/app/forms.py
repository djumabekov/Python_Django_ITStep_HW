"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from app.models import Authors, Books, Publishers, Publications, Sales


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class AuthorsForm(ModelForm):
    class Meta:
        model = Authors
        fields = ('FIO', 'birth_date')


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'genre', 'write_date', 'author')


class PublishersForm(ModelForm):
    class Meta:
        model = Publishers
        fields = ('name',)


class PublicationsForm(ModelForm):
    class Meta:
        model = Publications
        fields = ('count', 'date', 'publisher', 'book')


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ('price_for_one', 'count', 'date', 'publications', 'total_price_for_all')