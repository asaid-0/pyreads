from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 
            "username",
            "first_name",
            "last_name",
            "birth_date",
            "country",
            "mobile_phone",
            "facebook_account",
            "profile_picture",)

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ("first_name",
            "last_name",
            "birth_date",
            "country",
            "mobile_phone",
            "facebook_account",
            "profile_picture",)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'birth_date', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','featuring_date')
    list_filter = ('is_featured',)
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Project_pictures)
admin.site.register(Donation)


