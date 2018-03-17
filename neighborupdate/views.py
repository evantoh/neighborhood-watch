from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm,ProfileForm

from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.
@login_required
def welcome(request):
    return render(request,'all-temps/welcome.html')

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