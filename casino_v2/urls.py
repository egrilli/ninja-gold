from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('processMoney',views.processMoney),
    path('withdraw',views.withdraw),
    path('api-oro',views.oroData)

]