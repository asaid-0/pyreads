from django import forms
from users.models import Project, Project_pictures, Comment, Donation
from django.utils.translation import ugettext_lazy as _
import datetime

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
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date <= start_date:
            msg = "End date should be greater than start date."
            self.add_error("end_date", msg)
        elif end_date < datetime.date.today() or end_date == datetime.date.today():
            msg = "End date should be greater than today date."
            self.add_error("end_date", msg)

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
        labels = {"content": ""}
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "class": "comment-input",
                    "placeholder": "New Comment....",
                }
            ),
        }

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ("amount",)
        labels = {"amount": ""}
        widgets = {
            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "0",
                    "id":"amount"
                }
            ),
        }
