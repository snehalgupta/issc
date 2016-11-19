from django.conf.urls import include,url
#from django.contrib import admin
from . import views,models
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns=[
       url(r'^register',views.user_new,name='register'),
       url(r'^$', TemplateView.as_view(template_name='./dbms/home.html'), name='home'),
       url(r'^login/$', auth_views.login, {'template_name': './dbms/login.html'}, name='login'),
       url(r'^logout/$', auth_views.logout, {'template_name': './dbms/logged_out.html'}, name='logout'),	
       url(r'^export/(?P<prid>\D+)/$',views.ExportSubtask),
       url(r'^done/(?P<prid>\D+)/(?P<tid>\d+)/(?P<res>\d+)/$',views.GetData),
       url(r'^download/',views.Download),
       url(r'^igot/(?P<prid>\D+)/(?P<tid>\d+)/$',views.Change),
       url(r'^projectmgmt',views.projectmgmt,name='projectmgmt'),
       url(r'^download_file',views.download_file,name='download_file')

]
