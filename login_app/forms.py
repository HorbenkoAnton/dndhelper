from django.contrib.auth.forms import SetPasswordForm,UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')  

class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
