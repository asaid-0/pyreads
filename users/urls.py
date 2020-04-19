from django.urls import path
<<<<<<< HEAD
from .views import show_profile, edit_profile, get_projects, get_donations
=======
from .views import show_profile, edit_profile, home
>>>>>>> e7053141fd90d146fb92140b787597b87cadd9ee

urlpatterns = [
    path('', home, name='home'),
    path('users/<int:id>', show_profile, name='profile'),
    path('users/<int:id>/edit', edit_profile, name='edit_profile'),

    path('users/<int:id>/projects', get_projects , name='all_projects'),
    path('users/<int:id>/donations', get_donations , name='all_donations')



]
