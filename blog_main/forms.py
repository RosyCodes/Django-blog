from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        # creates a form based on User model/table
        model = User
        fields = ('email', 'username', 'password1', 'password2')
