from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = []

urlpatterns += i18n_patterns(
    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^drug/', include('drug.urls')),
    url(r'^checker/', include('checker.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^interactions/', include('interactions.urls')),
)
