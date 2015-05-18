from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UniqueEmailUser


class UniqueEmailUserCreationForm(UserCreationForm):
    """
    A form that creates a UniqueEmailUser.
    """

    def __init__(self, *args, **kargs):
        super(UniqueEmailUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = UniqueEmailUser
        fields = ("email",)


class UniqueEmailUserChangeForm(UserChangeForm):
    """
    A form for updating a UniqueEmailUser.
    """

    def __init__(self, *args, **kargs):
        super(UniqueEmailUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = UniqueEmailUser
        fields = ("email",)
