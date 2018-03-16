from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'all-temps/welcome.html')
def update_profile(request,user_id):
    user=User.objects.get(pk=user_id)
    user.profile.bio='ffgfdvnbdfgcbfghnhjykjm'
    user.save()