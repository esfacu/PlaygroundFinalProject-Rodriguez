from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Project)

admin.site.register(models.Task)

admin.site.register(models.Developers)

admin.site.register(models.Avatar)