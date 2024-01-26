from django.urls import path, include
from fitnew import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "fitnew"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('grupos_musculares/', views.ExercisesListView.as_view(), name='muscular_groups'),
    path('exercícios/<int:muscular_groups_id>', views.MuscularGroupsListView.as_view(), name='muscular_groups')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
