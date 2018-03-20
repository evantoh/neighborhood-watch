from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^create/profile$',views.update_profile,name='profile'),
    url(r'^post/create',views.post,name = 'posthood'),
    url(r'^business/create',views.business,name = 'postbusiness'),
    url(r'^business/view',views.view_business,name = 'viewBusiness'),
    url(r'^search/',views.search_bizna, name='search_bizna'),
]