# Generated by Django 3.2.5 on 2021-09-12 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_suburb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='suburb',
            field=models.CharField(choices=[(1, 'Anstead'), (2, 'Pullenvale'), (3, 'Kenmore')], max_length=2),
        ),
    ]
