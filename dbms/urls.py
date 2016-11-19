from django.conf.urls import include,url
#from django.contrib import admin
from . import views,models


urlpatterns=[
       url(r'^register',views.user_new,name='register'),
       url(r'^export/(?P<prid>\D+)/$',views.ExportSubtask),
       url(r'^done/(?P<prid>\D+)/(?P<tid>\d+)/(?P<res>\d+)/$',views.GetData),
       url(r'^download/',views.Download),
       url(r'^igot/(?P<prid>\D+)/(?P<tid>\d+)/$',views.Change),
       url(r'^projectmgmt',views.project_mgmt,name='projectmgmt'),
       url(r'^download_file',views.download_file,name='download_file')

]
