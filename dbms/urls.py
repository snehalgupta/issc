from django.conf.urls import include,url
#from django.contrib import admin
from . import views,models
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
       #url(r'^$',include(dbms.urls)
       url(r'^export/(?P<prid>\D+)/$',views.ExportSubtask),
       url(r'^(?P<prid>\D+)/done/(?P<tid>\d+)/(?P<res>\d+)/$',views.GetData),
       url(r'^download/',views.Download),
       url(r'^igot/(?P<prid>\D+)/(?P<tid>\d+)/$',views.Change),
       url(r'^done/(?P<prid>\D+)/(?P<tid>\d+)/$',csrf_exempt(views.GetFile))

]
