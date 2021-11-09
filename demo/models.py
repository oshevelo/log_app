import datetime
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=12)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=2000)
    author = models.ForeignKey(User, related_name='my_questions', on_delete=models.CASCADE, null=True, blank=True)
    respondent = models.ForeignKey(User, related_name='resp_questions', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.question_text
