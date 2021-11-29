from django.db import models


class Route(models.Model):
    name_route = models.TextField()
    start_point_lat = models.DecimalField(max_digits=10, decimal_places=10)
    start_point_long = models.DecimalField(max_digits=10, decimal_places=10)
    end_point_lat = models.DecimalField(max_digits=10, decimal_places=10)
    end_point_long = models.DecimalField(max_digits=10, decimal_places=10)
    journey_dist = models.IntegerField()
    journey_time = models.DateTimeField()
    journey_rating = models.IntegerField()

    def __str__(self):
        return self.name_route
