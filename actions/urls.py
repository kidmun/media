from django.urls import path
from . import views

urlpatterns=[
    path('messages/',views.messsagesPage,name="messages_page"),
    path('each_message/<str:pk>/',views.eachMessage,name="each_message"),

    path('add_contact/<str:pk1>/<str:pk2>/',views.addContact,name="add_contact")
]