from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url('^create_profile$',views.update_profile,name='profile'),
    url('^$',views.welcome,name = 'welcome'),
]