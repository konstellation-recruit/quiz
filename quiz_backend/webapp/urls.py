from django.urls import path
from django.conf.urls import url

# NOTE `from . import api_v1` would not work
from .views import api
from .views import quiz
from .views import index


urlpatterns = [
    path('v1/', api.urls),
    
    url(r'^$', index, name='index'),
    url(r'^quiz/', quiz, name='quiz'),
]
