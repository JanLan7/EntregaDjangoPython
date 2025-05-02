from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('send/', views.send_message, name='send_message'),
]
