from django.conf.urls import include,url
#from django.contrib import admin
from . import views,models
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt

path='.'
urlpatterns=[
       url(r'^register',views.user_new,name='register'),
       url(r'^$', TemplateView.as_view(template_name=path+'/dbms/home.html'), name='home'),
       url(r'^login/$', auth_views.login, {'template_name': path+'/dbms/login.html'}, name='login'),
       url(r'^logout/$', auth_views.logout, {'template_name': path+'/dbms/logged_out.html'}, name='logout'),
       url(r'^export/(?P<prid>\D+)/$',views.ExportSubtask),
       url(r'^done/(?P<prid>\D+)/(?P<tid>\d+)/(?P<res>\d+)/$',views.GetData),#urls for projects of type 1
       url(r'^download/(?P<prid>\D+)',views.Download),
       url(r'^igot/(?P<prid>\D+)/(?P<tid>\d+)/$',views.Change),
       url(r'^addproject',views.addproject,name='addproject'),
       url(r'^delproject',views.delproject,name='delproject'),
       url(r'^download_userfile/(?P<uid>[a-zA-Z0-9@.+-_]+)/$',views.download_userdata,name='download_file'),
       url(r'^done/(?P<prid>\D+)/(?P<tid>\d+)$',csrf_exempt(views.GetFile))

]
