from django.conf.urls import url
from .views import DrugInteractionCheckerApiListView, DrugInteractionCheckerApiDetailsView

urlpatterns = [
    url(r'^$', DrugInteractionCheckerApiListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DrugInteractionCheckerApiDetailsView.as_view()),
]
