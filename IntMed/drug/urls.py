from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DrugListView.as_view()),
    url(r'^create/$', views.DrugFormView.as_view()),
    url(r'^interactions/$', views.interactions),
    url(r'^export/$', views.export),
]
