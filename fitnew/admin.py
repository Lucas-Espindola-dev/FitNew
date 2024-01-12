from django.contrib import admin
from fitnew.models import MuscularGroup, Exercises


class MuscularGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(MuscularGroup, MuscularGroupsAdmin)


class ExercisesGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_exercise')


admin.site.register(Exercises, ExercisesGroupsAdmin)
