# Generated by Django 3.2.5 on 2021-09-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('projects', models.ManyToManyField(to='projects.Project')),
            ],
        ),
    ]
