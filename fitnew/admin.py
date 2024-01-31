from django.contrib import admin
from fitnew.models import MuscularGroup, Exercises, Lists


class MuscularGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(MuscularGroup, MuscularGroupsAdmin)


class ExercisesGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_exercise')


admin.site.register(Exercises, ExercisesGroupsAdmin)


class ListsAdmin(admin.ModelAdmin):
    list_display = ('id', 'list_name')


admin.site.register(Lists, ListsAdmin)
