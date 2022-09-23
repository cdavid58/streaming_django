from django.conf.urls import url
from .views import *

urlpatterns=[
	# url(r'^$',screen,name="screen"),
	url(r'^index/$',index,name="index"),
	url(r'^$',dynamic_stream,name="videostream"),
]