from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "birth_date",
            "country",
            "mobile_phone",
            "facebook_account",
            "profile_picture",
        )

