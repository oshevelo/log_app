import datetime
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=12)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question_text
