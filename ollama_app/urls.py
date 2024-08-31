from django.urls import path
from .views import ollama_chat

urlpatterns = [
    path('chat/', ollama_chat),
]
