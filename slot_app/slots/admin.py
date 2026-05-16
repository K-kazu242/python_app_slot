from django.contrib import admin
from .models import SlotRecord


@admin.register(SlotRecord)
class SlotRecordAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'memo', 'created_at']
    list_filter = ['date']
    ordering = ['-date']
