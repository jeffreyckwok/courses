from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),       # 'home' route.
    url(r'^addcourse$', views.addcourse),
    url(r'^destroy/(?P<id>\d+)?$', views.destroy),
    url(r'^delete/(?P<id>\d+)?$', views.delete),
]
