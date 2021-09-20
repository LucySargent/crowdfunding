from django.contrib import admin
from .models import Category, Project, Pledge, Beefriend


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Pledge)
admin.site.register(Beefriend)