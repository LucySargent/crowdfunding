# Generated by Django 3.2.5 on 2021-09-16 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_rename_goal_project_min_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='min_goal',
        ),
    ]
