from django.conf.urls import url
from . import views
#from django.conf import settings

urlpatterns = [
	url(r'^$', views.form),
   	url(r'^s', views.firecreate,name = 'create'),
   	url(r'^v',views.fireview, name= 'view'),
   	url(r'^d',views.firedelete, name= 'delete'),
]
