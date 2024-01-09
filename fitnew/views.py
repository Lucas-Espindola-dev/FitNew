from fitnew.models import Exercises
from django.views.generic import ListView, CreateView


class ExercisesListView(ListView):
    model = Exercises
    context_object_name = 'pages'


class ExercisesCreateView(CreateView):
    model = Exercises
