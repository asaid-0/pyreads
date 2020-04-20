from django.urls import path
from .views import add_project

urlpatterns = [
    path('project/new', add_project, name='add_project'),

]