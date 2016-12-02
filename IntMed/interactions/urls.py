from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^single/$', views.single),
    url(r'^single/(?P<id>[0-9]+)/$', views.single),
]
