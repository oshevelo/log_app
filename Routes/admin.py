from django.contrib import admin
from .models import Routes


class RoutesAdmin(admin.ModelAdmin):
    search_fields = ('id', 'start_point', 'end_point', 'distance', 'time', 'rating')
    list_display = ('id', 'start_point', 'end_point', 'distance', 'time', 'rating')
    list_display_links = ('id',)
    list_filter = ('distance', 'rating')


admin.site.register(Routes, RoutesAdmin)