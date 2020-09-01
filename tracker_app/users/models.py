import django.contrib.auth as dj_auth
from .models import User

class userCreationForm(dj_authforms.UserCreationForm):
    class Meta(dj_auth.froms.UserCreationsForm.Meta):
        model = User
        fields = dj_auth.forms.UserCreationForm.Meta.fields


class UserChangeForm(dj_auth.forms.UserChangeForm):
    class Meta(dj_auth.forms.UserChangeForm.Meta):
        model = User
        fields = dj_auth.forms.UserChangeForm.Meta.fields

class AuthenticationForm(dj_auth.formsAuthenticationForm):
    pass

class PasswordResetForm(dj_auth.formsPasswordResetForm):
    pass

class SetPasswordForm(dj_auth.forms.SetPasswordForm):
    pass

class PasswordChangeForm(dj_auth.forms.PasswordChangeForm):
    pass
