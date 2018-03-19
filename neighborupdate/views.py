from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm,ProfileForm,PostForm,BusinessForm
from .models import User,Profile,Post,Business

from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.
@login_required
def welcome(request):
    return render(request,'all-temps/welcome.html')

#a function that edits and create user profile at the same time
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('Your profile was successfully updated!')
            return HttpResponseRedirect('/')
        else:
            print('Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'all-temps/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

#function to help user post that will be available to all neighbours around him/her
def post(request):
    current_user=request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.user_id =  current_user
            # new_post.neighborhood_id = current_neighborhood
            new_post.save()
            return redirect('welcome') 
    else:
        form = PostForm()
    return render(request,'all-temps/post.html',{"form":form})
#function to create a business
def business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_business = form.save(commit = False)
            new_business.user_id =  current_user
            new_business.save()
            return redirect('welcome') 
    else:
        form = BusinessForm()
    return render(request,'all-temps/business/business.html',{"form":form})

#function to display businesses

def view_business(request):
    current_user = request.user
    businesses = Business.objects.all()
    return render(request,'all-temps/business/view_business.html',{"current_user":current_user,"businesses":businesses,})
