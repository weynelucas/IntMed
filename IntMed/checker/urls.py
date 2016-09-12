from django.conf.urls import url
from .views import DrugInteractionCheckerFormView, export

urlpatterns = [
    url(r'^create/$', DrugInteractionCheckerFormView.as_view()),
    url(r'^export/$', export),
]
