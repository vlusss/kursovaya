from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Orders


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field'}))
    date_joined = forms.DateTimeField(disabled=True, label='Дата регистрации',
                                      widget=forms.DateTimeInput(attrs={'class': 'input-field'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']


class MakeOrderForm(forms.ModelForm):

    rent_time = forms.IntegerField(widget=forms.NumberInput(attrs={'onchange': "calculate_total_price();",
                                                                   'value': 600,
                                                                   'class': 'input-field'}))

    class Meta:
        model = Orders
        fields = ['rent_time', ]
