from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    neigh_location = models.CharField(max_length=30, blank=True)
    neigh_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username
   

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# create model neighborhood
# class Neighbourhood(models.Model):
#     neighborhood_name = models.CharField(max_length =30)
#     neighborhood_location = models.CharField(max_length =30)
#     occupants_count = models.IntegerField(default=0)
#     admin=models.ForeignKey(User,null=True)

    