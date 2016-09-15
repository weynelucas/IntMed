from django.conf.urls import url
from .views import DrugApiListView

urlpatterns = [
    url(r'^$', DrugApiListView.as_view()),
]
