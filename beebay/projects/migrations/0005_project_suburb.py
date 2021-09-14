# Generated by Django 3.2.5 on 2021-09-12 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_adopt_beefriend'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='suburb',
            field=models.CharField(choices=[(1, 'Anstead'), (2, 'Pullenvale'), (3, 'Kenmore')], default=1, max_length=2),
        ),
    ]