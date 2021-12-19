from .models import (User, Question, Answer)
from utils import admin_default

for model in (User, Question, Answer):
    admin_default(model)
