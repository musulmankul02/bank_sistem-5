from django.contrib import admin
from .models import HistoryTransfer

@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('id','from_user', 'to_user', 'amount', 'is_completed', 'created_at')

