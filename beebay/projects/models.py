from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    beehives = models.IntegerField(null=True)
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, #if i delete the user, delete their projects too
        related_name='owner_projects'
    )
    # min_required = models.IntegerField() 

    @property
    def goal(self):
        return self.beehives * 300


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    #point supporter to the user
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
    beefriender = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='befriender'
    )