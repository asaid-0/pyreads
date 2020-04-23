from django.urls import path
from .views import add_project, view_project, add_comment, delete_project, get_category_projects

urlpatterns = [
    path('project/new', add_project, name='add_project'),
    path('project/<int:id>', view_project, name='view_project'),
    path('project/<int:id>/delete', delete_project, name='delete_project'),
    path('project/<int:id>/comment', add_comment, name='add_comment'),
    path('category/<int:id>/projects', get_category_projects , name='category_projects')


]