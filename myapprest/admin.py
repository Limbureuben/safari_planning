from django.contrib import admin
from .models import *


class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ()
