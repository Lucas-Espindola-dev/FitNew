from django.contrib import admin
from fitnew.models import MuscularGroup


class MuscularGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(MuscularGroup, MuscularGroupsAdmin)


