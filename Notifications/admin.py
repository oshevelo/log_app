from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    raw_id_fields = ('recipient', 'owner',)

admin.site.register(Notification, NotificationAdmin)
