from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('account/<str:pk>/',views.account,name="account"),
]
