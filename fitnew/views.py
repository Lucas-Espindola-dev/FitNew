from fitnew.models import Exercises, MuscularGroup, Lists
from django.views.generic import ListView
from django.shortcuts import render


def home(request):
    return render(request, 'fitnew/pages/home.html')


class ExercisesListView(ListView):
    model = Exercises
    template_name = 'fitnew/pages/exercises.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        exercises = super().get_queryset().filter(muscular_group__id=self.kwargs['muscular_groups_id']).order_by('-id')
        return exercises


class MuscularGroupsListView(ListView):
    model = MuscularGroup
    template_name = 'fitnew/pages/muscular_groups.html'
    context_object_name = 'muscular_groups'


class ListsExercisesListview(ListView):
    model = Lists
    template_name = 'fitnew/pages/exercises_lists.html'
    context_object_name = 'exercises_lists'

    def get_queryset(self):
        lists = super().get_queryset().order_by('list_name')
        return lists
