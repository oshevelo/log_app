from django.contrib import admin

from .models import Room, Message


class MessageAdmin(admin.ModelAdmin):
    raw_id_fields = ['room']


admin.site.register(Message, MessageAdmin)


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    search_fields = ['room_text']
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None, {'fields': ['room_text', 'description']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('room_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    inlines = [MessageInline]


admin.site.register(Room, RoomAdmin)