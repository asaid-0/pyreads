from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Project_pictures)
admin.site.register(Project_tags)

