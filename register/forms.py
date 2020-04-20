from django.contrib.auth.forms import UserCreationForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
        fields += (
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "country",
            "mobile_phone",
            # "profile_picture",
            )
