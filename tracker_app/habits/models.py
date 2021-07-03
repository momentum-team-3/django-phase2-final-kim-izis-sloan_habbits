from django.db import models
from users.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_description = models.TextField()
    goal_count = models.IntegerField(null=False, blank=False)
