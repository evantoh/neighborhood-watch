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

class Business(models.Model):
    business_name = models.CharField(max_length =30,null=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  
    neighborhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null= True)
    business_email = models.EmailField(null=True)
    business_description = models.TextField(null= True )

    def __str__(self):
        return self.business_name  

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self,business_name,business_email):
        self.business_name = business_name
        self.business_email = business_email
        self.save() 

    @classmethod
    def find_business(cls,business_id):
            found_business = cls.objects.get(id= business_id)
            return found_business

    @classmethod
    def all_business(cls):
        found_business = cls.objects.all()
        return found_business

    @classmethod
    def search_by_business(cls,business_name):
        searched_bizna = cls.objects.filter(business_name__icontains = business_name)
        return searched_bizna

class Post(models.Model):
    

    title = models.CharField(max_length =30,null=True) 
    post = models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    neighborhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null= True)
    post_date = models.DateTimeField(auto_now_add=True, null= True)


    def __str__(self):
        return self.title

    @classmethod
    def get_all_post(cls):
        posts = cls.objects.all()
        return posts

    class Meta:
        ordering = ['-post_date']