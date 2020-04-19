from django.urls import path
from .views import show_profile, edit_profile, get_projects, get_donations, home

urlpatterns = [
    path('', home, name='home'),
    path('users/<int:id>', show_profile, name='profile'),
    path('users/<int:id>/edit', edit_profile, name='edit_profile'),

    path('users/<int:id>/projects', get_projects , name='all_projects'),
    path('users/<int:id>/donations', get_donations , name='all_donations')



]
