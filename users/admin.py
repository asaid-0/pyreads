from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','featuring_date')
    list_filter = ('is_featured',)
# Register your models here.
admin.site.register(User)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Project_pictures)
admin.site.register(Project_tags)
admin.site.register(Donation)


