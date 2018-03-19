from django import forms
from .models import User,Profile,Post

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