from django.conf.urls import url, include
from .views import DrugInteractionCheckerFormView, export

urlpatterns = [
    url(r'^create/$', DrugInteractionCheckerFormView.as_view()),
    url(r'^export/$', export),
]
