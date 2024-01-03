from django.db import models


class MuscularGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Exercises(models.Model):
    id = models.AutoField(primary_key=True)
    name_exercise = models.CharField(max_length=150)
    series = models.IntegerField()
    reps = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='exercices/', blank=True, null=True)
    muscular_group = models.ForeignKey(MuscularGroup, on_delete=models.PROTECT,
                                       related_name='muscular_group', default=None)

    def __str__(self):
        return self.name_exercise
