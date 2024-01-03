# Generated by Django 5.0.1 on 2024-01-03 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnew', '0003_exercises_muscular_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='muscular_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='muscular_groups', to='fitnew.musculargroup'),
        ),
    ]
