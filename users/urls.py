from django.urls import path
from .views import show_profile, edit_profile, get_projects, get_donations, home, get_category_projects

urlpatterns = [
    path('', home, name='home'),

    path('category/<int:id>/projects', get_category_projects , name='category_projects'),


    path('users/<int:id>', show_profile, name='profile'),
    path('users/<int:id>/edit', edit_profile, name='edit_profile'),
    path('users/<int:id>/projects', get_projects , name='user_projects'),
    path('users/<int:id>/donations', get_donations , name='user_donations')





]
