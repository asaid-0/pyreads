from django.urls import path
from .views import add_project, view_project

urlpatterns = [
    path('project/new', add_project, name='add_project'),
    path('project/<int:id>', view_project, name='view_project'),

]