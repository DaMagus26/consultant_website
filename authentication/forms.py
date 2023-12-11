from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class_attr = 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class': class_attr, 'placeholder': ''}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': class_attr, 'placeholder': ''}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': class_attr, 'placeholder': ''}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class CustomAuthenticationForm(forms.Form):
    class_attr = 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': class_attr, 'placeholder': ''}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': class_attr, 'placeholder': ''}))
