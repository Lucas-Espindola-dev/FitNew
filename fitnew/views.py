from fitnew.models import Exercises
from django.views.generic import ListView
from django.shortcuts import render


def home(request):
    return render(request, 'fitnew/pages/home.html')


class ExercisesListView(ListView):
    model = Exercises
    template_name = 'fitnew/pages/exercises.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        exercises = super().get_queryset().order_by('name_exercise')
        muscular_groups = self.request.GET.get('muscular_group')


