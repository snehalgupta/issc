from django.conf.urls import include,url
#from django.contrib import admin
from . import views,models


urlpatterns=[
       url(r'^$',include(dbms.urls)
       url(r'^export/(?P<tid>\d+)/$',views.ExportSubtask),
       url(r'^done/(?P<tid>\d+)/(?P<res>\d+)/$',views.GetData),
       url(r'^download/',views.Download),
       url(r'^igot/(?P<prid>\d+)/(?P<tid>\d+)/$',views.Change)

]
