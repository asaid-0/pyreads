from django import forms
from users.models import Project

class AddProjectForm(forms.ModelForm):
    class Meta:
        model =Project
        fields = (
            'title',
            'details',
            'total_target',
            'start_date',
            'end_date',
            'category',
        )