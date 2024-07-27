from django import forms as d_forms
from allauth.account.forms import SignupForm, ResetPasswordForm, LoginForm
from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):
    """
    Sign Up form for the account
    """
    username = d_forms.CharField(
        max_length=30,
        label='Username',
        widget=d_forms.TextInput(
            attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'})
    )
    first_name = d_forms.CharField(
        max_length=30,
        label='First Name',
        widget=d_forms.TextInput(
            attrs={
                'placeholder': 'Enter your first name',
                'class': 'form-control'})
    )
    last_name = d_forms.CharField(
        max_length=30,
        label='Last Name',
        widget=d_forms.TextInput(
            attrs={
                'placeholder': 'Enter your last name',
                'class': 'form-control'})
    )
    email = d_forms.EmailField(
        max_length=254,
        label='Email',
        widget=d_forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control'})
    )
    password1 = d_forms.CharField(
        label='Password',
        widget=d_forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'class': 'form-control'})
    )
    password2 = d_forms.CharField(
        label='Password (again)',
        widget=d_forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your password',
                'class': 'form-control'})
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise d_forms.ValidationError(
                "A user with that email already exists.")
        return email


class CustomLoginForm(LoginForm):
    """
    Login form
    """
    login = d_forms.CharField(
        max_length=254,
        label='Username',
        widget=d_forms.TextInput(
            attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'})
    )
    password = d_forms.CharField(
        label='Password',
        widget=d_forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'class': 'form-control'})
    )
    remember = d_forms.BooleanField(
        label='Remember Me',
        required=False,
        widget=d_forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class CustomPasswordResetForm(ResetPasswordForm):
    """
    Password Reset form for the Forgot Password? option
    """
    email = d_forms.EmailField(
        max_length=254,
        label='Email',
        widget=d_forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email address'})
    )
