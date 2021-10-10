from django.db import models

# Create your models here.


class Routes(models.Model):
    start_point = models.CharField(max_length=50) # x, y = '0, 0' example in string
    end_point = models.CharField(max_length=50) # x, y = '10, 10' example in string
    distance = models.IntegerField() # min_dist | max_dist
    time = models.TimeField() # time to
    rating = models.IntegerField() #