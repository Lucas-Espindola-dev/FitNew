# Generated by Django 5.0.1 on 2024-01-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='exercises',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_exercise', models.CharField(max_length=150)),
                ('series', models.IntegerField()),
                ('reps', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='exercices/')),
            ],
        ),
    ]
