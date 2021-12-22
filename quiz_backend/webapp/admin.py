from .models import (User, Question, Answer)
from .utils import admin_default

for model in (User, Question):
    admin_default(model)

admin_default(Answer, readonly_fields=('datetime',))
