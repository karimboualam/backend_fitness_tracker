from django.contrib import admin
from .models import Progress

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'metric', 'value', 'date')
    list_filter = ('metric', 'date')
    search_fields = ('user__username', 'metric')
