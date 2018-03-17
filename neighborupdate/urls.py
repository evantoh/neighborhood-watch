from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url('^$',views.update_profile,name='profile'),
    url('^welcome$',views.welcome,name = 'welcome'),
]