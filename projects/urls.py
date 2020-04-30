from django.urls import path
from .views import add_project, view_project, add_comment, add_reply, delete_project, get_category_projects, add_donation, report_comment, report_project, add_rate, search_by_tag_title

urlpatterns = [
    path('project/new', add_project, name='add_project'),
    path('project/<int:id>', view_project, name='view_project'),
    path('project/<int:id>/delete', delete_project, name='delete_project'),
    path('project/<int:id>/comment', add_comment, name='add_comment'),
    path('project/<int:id>/reply', add_reply, name='add_reply'),
    path('category/<int:id>/projects', get_category_projects , name='category_projects'),
    path('project/ajax/donation', add_donation, name='donate'),
    path('comment/<int:id>/report', report_comment, name='report_comment'),
    path('project/<int:id>/report', report_project, name='report_project'),
    path('project/search', search_by_tag_title, name="search"),
    path('project/ajax/rate', add_rate, name='rate')
]