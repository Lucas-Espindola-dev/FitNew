from django.urls import path, include
from fitnew.views import *

urlpatterns = [
    path('home/', ExercisesListView.as_view(), name='home'),
]
