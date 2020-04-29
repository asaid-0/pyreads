from django.urls import path
from .views import show_profile, edit_profile, delete_account, get_projects, get_donations, home, get_categories
from projects.views import get_category_projects
urlpatterns = [
    path('', home, name='home'),
    path('profile/', show_profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/delete', delete_account, name='delete_account'),
    path('user/projects', get_projects , name='user_projects'),
    path('user/donations', get_donations , name='user_donations'),
    path('categories/', get_categories , name='get_categories'),

]
