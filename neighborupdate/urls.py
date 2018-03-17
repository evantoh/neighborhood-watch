from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^prof$',views.update_profile,name='profile'),
]