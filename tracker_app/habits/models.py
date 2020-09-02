from django.db import models
from django.contrib.auth.models import User
import time
from datetime import date

class Habits(models.Model):
    name = models.CharField(max_length=50)
    goal = models.IntegerField()
    unit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=date.today())
    owner = models.ForeignKey(to=User, related_name='owner', null=True, on_delete=models.CASCADE)
    observer = models.ForeignKey(to=User, related_name='observer', on_delete=models.CASCADE, null=True, blank=True)

    def __str__ (self):
        return self.name

class HabitsRecord(models.Model):
    habit = models.ForeignKey('Habits', on_delete=models.CASCADE, null=True, blank=True, related_name='habit_records')
    progress = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(default=date.today())

    def __str__ (self):
        return f'This is the record for {self.habits}.'
    
    class Meta:
        unique_together = ('due_date', 'habits')