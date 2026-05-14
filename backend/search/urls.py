from django.urls import path
from .views import search_view, health_view

urlpatterns = [
    path("search/", search_view),
    path("health/", health_view)
]