from django.urls import path, include
from fitnew import views


app_name = "fitnew"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('exercicios/', views.ExercisesListView.as_view(), name='exercises')
]
