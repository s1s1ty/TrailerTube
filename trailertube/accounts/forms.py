from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    def authenticate(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        if username and password:
            return authenticate(username=username, password=password)
    def clean(self, *args, **kwargs):
        user = self.authenticate()
        if not user:
            raise forms.ValidationError("This User doesnot Exist or Incorrect Password.")
        if not user.is_active:
            raise forms.ValidationError("This user is no longer active.")
        return super(LoginForm, self).clean(*args, **kwargs)
        
class JoinForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "confirm_password"
        ]

    def clean_confirm_password(self):
        """
        Check password matching
        """
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']
            if password == confirm_password:
                return password
            raise forms.ValidationError('Password and Confirm Password donot match.')

    def clean_email(self):
        """
        enforces uniqueness of email addresses.
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError("This Email address already register.")
        return email
