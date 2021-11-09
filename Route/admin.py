from django.contrib import admin
from .models import Route


class RouteAdmin(admin.ModelAdmin):
    search_fields = ('id', 'start_point_x', 'start_point_y', 'end_point_x', 'end_point_y', 'distance', 'date_time', 'rating')
    list_display = ('id', 'start_point_x', 'start_point_y', 'end_point_x', 'end_point_y', 'distance', 'date_time', 'rating')
    list_display_links = ('id',)
    list_filter = ('distance', 'rating')


admin.site.register(Route, RouteAdmin)