from django.contrib import admin
from . models import Task
# Register your models here.
@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date','completed', 'priority','create_at']
    search_fields = ['title']
    list_filter = ['completed', 'priority']