from django.conf.urls import url
from .views import DrugInteractionCheckerApiListView

urlpatterns = [
    url(r'^$', DrugInteractionCheckerApiListView.as_view()),
]
