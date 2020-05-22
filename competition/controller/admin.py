from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Students, Admins

# Register your models here.
admin.site.register(Students)
admin.site.register(Admins)