from django.conf.urls import url
from . import quiz_processor
from . import quizquiz


websocket_urlpatterns = [
    # url(r'^ws/quiz/', quiz_processor.QuizProcessor.as_asgi())
    url(r'^ws/quiz/', quizquiz.QuizQuizConsumer.as_asgi())
]
