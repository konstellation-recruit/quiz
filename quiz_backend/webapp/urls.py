from django.urls import path

# NOTE `from . import api_v1` would not work
from .views import api


urlpatterns = [
    path('v1/', api.urls),
]
