from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.DiseaseListView.as_view()),
    url(r'^create/$', views.DiseaseFormView.as_view()),
]
