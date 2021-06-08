from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('app_v2/', include("casino_v2.urls")),
]
