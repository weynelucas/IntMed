from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/$', views.SignInFormView.as_view()),
    url(r'^signup/$', views.signup),
    url(r'^logout/$', views.logout),
]
