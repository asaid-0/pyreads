from django.urls import path
from .views import show_profile, edit_profile

urlpatterns = [
    path('users/<int:id>', show_profile, name='profile'),
    path('users/<int:id>/edit', edit_profile, name='edit_profile')
]
