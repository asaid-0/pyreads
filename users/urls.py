from django.urls import path
from .views import show_profile, edit_profile, delete_account, get_projects, get_donations, home, get_category_projects

urlpatterns = [
    path('', home, name='home'),

    path('category/<int:id>/projects', get_category_projects , name='category_projects'),


    path('profile/', show_profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/delete', delete_account, name='delete_account'),
    path('user/projects', get_projects , name='user_projects'),
    path('user/donations', get_donations , name='user_donations')





]
