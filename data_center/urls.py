from django.contrib import admin
from django.urls import path
from .views import Home


app_name = "celery_test"
urlpatterns = [
    path("", Home.as_view(), name="home")
]
