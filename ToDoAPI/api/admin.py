from django.contrib import admin
from .models import Task


# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'completed', 'author']
    list_filter = ['author', 'completed', 'data_create']
    search_fields = ['title', 'author']
