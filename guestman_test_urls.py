"""Minimal URL config for Guestman tests."""

from django.urls import include, path

urlpatterns = [
    path("api/guestman/", include("shopman.guestman.api.urls")),
]
