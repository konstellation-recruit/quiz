import datetime as dt

from ninja import Field, NinjaAPI, Schema

from .models import User, Question, Answer

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

api = NinjaAPI(version="1.0.0")


class SelectIn(Schema):
    user_id: int
    question_id: int
    selection: str


def index(
    request
    ) -> HttpResponse:
    # return JsonResponse({})
    return render(request, 'index.html', {})
    # pass

def quiz(
    request
    ) -> HttpResponse:
    # return render(request, "{}")
    # question = Question.objects.get(id=question_id)
    return render(request, 'quiz.html', {})


# 
@api.post("/select/")
def select(request, select_data: SelectIn):
    try:
        user_id, question_id = select_data.user_id, select_data.question_id

        user = User.objects.get(id=user_id)
        question = Question.objects.get(id=question_id)

        answer: Answer
        answer, _ = Answer.objects.get_or_create(
            user=user, question=question)

        assert select_data.selection in (Answer.SELECTION_O, Answer.SELECTION_X)

        answer.selection = select_data.selection
        answer.save()

        return {'success': True}

    except Exception as e:
        return {'success': False, 'error_msg': str(e)}
