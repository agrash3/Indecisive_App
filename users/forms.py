<<<<<<< HEAD
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Required is True in default. So i keep it default

    class Meta:
        model = User # Whenever the form is validate it is going to create a new user
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # This For Additional Field

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
=======
# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', )

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name', 'dob', 'location' ]
        widgets = { 'dob': DatePickerInput() }
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
