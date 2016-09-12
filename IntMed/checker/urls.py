from django.conf.urls import url
from .views import DrugInteractionCheckerFormView

urlpatterns = [
    url(r'^create/$', DrugInteractionCheckerFormView.as_view()),
]
