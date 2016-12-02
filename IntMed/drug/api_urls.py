from django.conf.urls import url
from .views import DrugApiListView, DrugApiDetailsView

urlpatterns = [
    url(r'^$', DrugApiListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DrugApiDetailsView.as_view()),
]
