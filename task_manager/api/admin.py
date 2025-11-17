from django.contrib import admin
from .models import Project, Task
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'owner_username')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project' 'status', 'assignee', 'created_at')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
