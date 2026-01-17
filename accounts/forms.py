

from django import forms
from accounts.models import Account


class RegistrationForm(forms.ModelForm):
    # These two fields are not part of the model.
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        # Mandatory fields
        # which model the form is based on.
        model = Account
        # the fields we want to show in the form.
        fields = ['first_name', 'last_name',
                  'email', 'password', 'phone_number']

    #    call the __init__ method to override the parent method to add placeholders and CSS classes
    def __init__(self, *args, **kwargs):
        # Ensures the fields exist before you modify them
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        #    Applying form-control for all fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    # Checking the password and confirm password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
