from django.conf.urls import include,url
#from django.contrib import admin
#from rest_framework.urlpatterns import format_suffix_patterns
import views,models


urlpatterns=[
       url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
       #url(r'^$',include(dbms.urls)
       url(r'^export/',views.Exportlist.as_view()),
       url(r'^done/(?P<tid>\d+)/(?P<res>\d+)/$',views.GetData),
       url(r'^download/',views.Download)

]
