from .views import SignInFormView
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/$', SignInFormView.as_view()),
]
