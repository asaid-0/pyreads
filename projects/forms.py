from django import forms
from users.models import Project, Project_pictures

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'details',
            'total_target',
            'start_date',
            'end_date',
            'category',
        )

class ImageForm(forms.ModelForm):
    class Meta:
        model= Project_pictures
        fields = ('picture',)
        widgets = {
            'picture': forms.ClearableFileInput(attrs={'multiple': True}),
        }