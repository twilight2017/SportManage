from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Students, Admins, Competitions, Notices

# Register your models here.
admin.site.register(Students)
admin.site.register(Admins)
admin.site.register(Competitions)
admin.site.register(Notices)