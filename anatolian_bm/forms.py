from django import forms as d_forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):

    first_name = d_forms.CharField(max_length = 25, label='First Name', required=True)
    last_name = d_forms.CharField(max_length = 25, label='Last Name', required=True)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        # Add your own processing here.
    
        # You must return the original result.
        return user
