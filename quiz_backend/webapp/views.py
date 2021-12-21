import datetime as dt

from ninja import Field, NinjaAPI, Schema, ModelSchema

from .models import User, Question, Answer

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

api = NinjaAPI(version="1.0.0")


class UpdateOrCreateUserIn(Schema):
    name: str
    email: str


class UserOut(ModelSchema):
    # TODO define serializer
    class Config:
        model = User
        model_fields = ['id', 'name', 'email', 'score']
        # json_encoders = { dt.datetime: lambda a: str(a) }


@api.post("/update_or_create_user/", response=UserOut)
def update_or_create_user(request, data: UpdateOrCreateUserIn):
    user, _ = User.objects.update_or_create(
        email=data.email,
        defaults={'name': data.name}
    )

    return user


@api.get('/get_user/{user_id}', response=UserOut)
def get_user(request, user_id: int):
    return User.objects.get(id=user_id)


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
