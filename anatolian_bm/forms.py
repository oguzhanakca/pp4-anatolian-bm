from django import forms as d_forms
from allauth.account.forms import SignupForm
class CustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        # Add your own processing here.
    first_name = d_forms.CharField(max_length = 25, label='First Name')
    last_name = d_forms.CharField(max_length = 25, label='Last Name')
    def signup(self,request,user):
            
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # You must return the original result.
        return user
