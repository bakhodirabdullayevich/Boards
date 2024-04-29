from django.contrib import admin
from .models import Board


# Register your models here.
'''class Board(admin.ModelAdmin):
    list_display = ('name', 'description')'''


admin.site.register(Board)