from django.conf.urls import url
from . import quiz_processor

websocket_urlpatterns = [
    url(r'^ws/quiz/', quiz_processor.QuizProcessor.as_asgi())
]