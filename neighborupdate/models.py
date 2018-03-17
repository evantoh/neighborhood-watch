from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


#  create model neighborhood
class Neighbourhood(models.Model):
    neigh_name = models.CharField(max_length =30,null=True)
    neigh_location= models.CharField(max_length =30,null=True)
    occupants_count = models.IntegerField(default=0)
    admin=models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.neigh_name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete() 
    
    def update_neighborhood(self,neigh_name,neigh_location,occupants_count):
        self.neighborhood_name = neighborhood_name
        self.neighborhood_location = neighborhood_location
        self.occupants_count += occupants_count
        self.save()

    @classmethod
    def find_neighbourhood(cls,neighborhood_id):
        '''
        Method the find_neighborhood method using the neighborhood id 
        '''
        found_neighbourhood = cls.objects.get(id = neighborhood_id)
        return found_neighborhood

    @classmethod
    def all_neighbourhoods(cls):
        '''
        Method that returns all the neighborhoods
        '''
        all_neighbourhoods = cls.objects.all()
        return all_neighbourhoods

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    neigh_location = models.CharField(max_length=30, blank=True)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null= True)
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

#