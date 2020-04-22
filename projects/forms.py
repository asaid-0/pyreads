from django import forms
from users.models import Project, Project_pictures, Comment
from django.utils.translation import ugettext_lazy as _


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "details",
            "total_target",
            "start_date",
            "end_date",
            "category",
            "tags",
        )
        widgets = {
            "tags": forms.TextInput(attrs={"data-role": "tagsinput", "name": "tags"}),
            "details": forms.Textarea(attrs={"rows": 7, "style": "resize:none;"}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Project_pictures
        fields = ("picture",)
        labels = {"picture": "Images"}
        widgets = {
            "picture": forms.ClearableFileInput(attrs={"multiple": True}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {"content": ''}
        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control", "style": "border: none; border-radius: 0", "placeholder": 'New Comment....'}),
        }