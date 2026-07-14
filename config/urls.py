from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/cinetrack/", permanent=False)),
    path("admin/", admin.site.urls),
    path("cinetrack/", include("cinetrack.urls", namespace="cinetrack")),
]