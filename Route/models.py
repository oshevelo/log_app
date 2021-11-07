from django.db import models

# Create your models here.


class Route(models.Model):
    name = models.TextField()
    start_point_x = models.DecimalField(max_digits=10, decimal_places=10)
    start_point_y = models.DecimalField(max_digits=10, decimal_places=10)
    end_point_x = models.DecimalField(max_digits=10, decimal_places=10)
    end_point_y = models.DecimalField(max_digits=10, decimal_places=10)
    distance = models.IntegerField()  # min_dist | max_dist
    date_time = models.DateTimeField()  # time to
    rating = models.IntegerField()  #

    def __str__(self):
        return self.name
