from django import forms
from .models import User,Profile,Post,Business

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = ('bio', 'neigh_location', 'neigh_name')

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ['title','post']

class BusinessForm(forms.ModelForm): 
    '''
    class that creates a new business creation form
    '''
    class Meta:
        model = Business
        fields = ['business_name','business_email','business_description']