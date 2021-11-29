from django.contrib import admin
from .models import Route


class RouteAdmin(admin.ModelAdmin):
    search_fields = ('id', 'start_point_lat', 'start_point_long', 'end_point_lat', 'end_point_long',
                     'journey_dist', 'journey_time', 'journey_rating')
    list_display = ('id', 'start_point_lat', 'start_point_long', 'end_point_lat', 'end_point_long',
                    'journey_dist', 'journey_time', 'journey_rating')
    list_display_links = ('id',)
    list_filter = ('journey_dist', 'journey_rating')


admin.site.register(Route, RouteAdmin)
