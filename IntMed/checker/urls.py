from django.conf.urls import url, include
from rest_framework import routers
from .views import DrugInteractionListView, DrugInteractionCheckerFormView, export

router = routers.SimpleRouter()
router.register(r'list', DrugInteractionListView)

urlpatterns = [
    url(r'^create/$', DrugInteractionCheckerFormView.as_view()),
    url(r'^export/$', export),
]

urlpatterns += router.urls
