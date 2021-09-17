from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    # suburb_choices = [
    #     (1, 'Anstead'),
    #     (2, 'Pullenvale'),
    #     (3, 'Kenmore'),
    # ]
    # suburb = models.CharField(
    #     max_length=2,
    #     choices=suburb_choices,
    # )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects',
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    

class Beefriend(models.Model):
    comment = models.CharField(max_length=200)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='adoptions'
        )
    supporter = models.CharField(max_length=200)