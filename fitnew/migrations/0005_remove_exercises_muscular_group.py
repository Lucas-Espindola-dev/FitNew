# Generated by Django 5.0.1 on 2024-01-03 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitnew', '0004_alter_exercises_muscular_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercises',
            name='muscular_group',
        ),
    ]
