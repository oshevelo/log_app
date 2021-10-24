from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_filter = ('user', 'recipient')
    raw_id_fields = ('user', 'recipient')
    search_fields = ('id', 'body', 'user__username', 'recipient__username')
    list_display = ('id', 'user', 'recipient', 'body', 'timestamp')
    list_display_links = ('id',)
    readonly_fields = ('timestamp',)
    date_hierarchy = 'timestamp'


admin.site.register(Message, MessageAdmin)
