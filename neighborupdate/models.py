from django.db import models

# Create your models here.
# create model neighborhood
class Neighbourhood(models.Model):
    neighborhood_name = models.CharField(max_length =30)
    neighborhood_location = models.CharField(max_length =30)
    occupants_count = models.IntegerField(default=0)
    admin=models.ForeignKey(User,null=True)

    