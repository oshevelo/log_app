from django.contrib import admin
from .models import Message, GroupChat


class MessageAdmin(admin.ModelAdmin):
    list_filter = ('sender', 'recipient')
    raw_id_fields = ('group_chat', 'sender', 'recipient')
    search_fields = ('id', 'body', 'sender__username', 'recipient__username')
    list_display = ('id', 'group_chat', 'sender', 'recipient', 'body', 'timestamp')
    list_display_links = ('id',)
    readonly_fields = ('timestamp',)
    date_hierarchy = 'timestamp'


class GroupChatAdmin(admin.ModelAdmin):
    list_filter = ('owner', 'participants')
    list_display = ('name',  'owner', 'description', 'image')
    search_fields = ('id', 'name', 'owner', 'participants')
    raw_id_fields = ('owner', 'participants')


admin.site.register(Message, MessageAdmin)
admin.site.register(GroupChat, GroupChatAdmin)
