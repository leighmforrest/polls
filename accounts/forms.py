from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, AdminUserCreationForm


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeform(UserChangeForm):
    model = get_user_model()
    fields = (
        "email",
        "username",
    )