from django.conf.urls import url
from .view import DrugInteractionCheckerFormView

urlpatterns = [
    url(r'^create/$', DrugInteractionCheckerFormView.as_view()),
]
