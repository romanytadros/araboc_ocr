from django.contrib import admin
from django.urls import include, path
from .views import homepage, webmains

urlpatterns = [
    path("", homepage, name="homepage"),
    # path("",webmains)
]
