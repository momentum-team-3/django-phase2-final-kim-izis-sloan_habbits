from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from users.models import User
from .models import Habit # , HabitRecord
from .forms import HabitForm # , HabitRecordForm


@login_required
def habit_list(request):
  habits = Habit.objects.filter(user=request.user)
  return render(request, 'habits/list_habits.html', {'habits': habits})


# There might be some naming missmatch you can change what ever you need
@login_required
def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'habits/habit_detail.html', {"habit": habit, "pk": pk})


@login_required
def habit_new(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect('habit_detail', pk=habit.pk)
    else:
        form = HabitForm()

    return render(request, 'habits/habit_new.html', {"form": form})


@login_required
def habit_edit(request, pk):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect('habit_detail', pk=habit.pk)
    else:
        form = HabitForm()

    return render(request, 'habits/edit_habit.html', {"form": form})   


@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habit_list')

