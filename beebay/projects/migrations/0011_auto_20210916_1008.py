# Generated by Django 3.2.5 on 2021-09-16 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='min_goal',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
