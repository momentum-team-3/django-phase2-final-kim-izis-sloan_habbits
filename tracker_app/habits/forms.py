  
from django import forms

from .models import Habit #, Log


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('goal_description', 'goal_count')

"""
class ActivityForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ('habit', 'activity_date', 'log_value', 'comments')
"""