from django.conf.urls import url, include

urlpatterns = [
    url(r'^drug/', include('drug.api_urls')),
    url(r'^checker/', include('checker.api_urls')),
]
