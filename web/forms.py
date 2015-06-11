from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UniqueEmailUser


class UniqueEmailUserCreationForm(UserCreationForm):
    """
    A form that creates a UniqueEmailUser.
    """

    class Meta:
        model = UniqueEmailUser
        fields = ("email",)


class UniqueEmailUserChangeForm(UserChangeForm):
    """
    A form for updating a UniqueEmailUser.
    """

    class Meta:
        model = UniqueEmailUser
        fields = ("email",)
