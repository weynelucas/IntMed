from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.MedicineListView.as_view()),
    url(r'^create/$', views.MedicineFormView.as_view()),
    url(r'^drugs_interaction/$', views.drugs_interaction),
]
