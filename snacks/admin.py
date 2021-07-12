from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Snack

admin.site.register(Snack)
# Register your models here.
