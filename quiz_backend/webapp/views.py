import datetime as dt

from ninja import Field, NinjaAPI, Schema, ModelSchema

from .models import User, Question, Answer


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


def update_scores():
    """
    This function is dumb in a sense that it will repeat iterating the
    same question assuming you will call this several time. But the computation
    will be trivial enough and it gaurantess the sum is correct, so we will
    stick with dum implementation.
    """
    new_user_scores = {}
    new_user_extra_scores = {}

    for question in Question.objects.all():
        correct_answer = question.correct_answer

        cur_extra = 63
        for answer in question.answer_set.all():
            user = answer.user

            if answer.selection == correct_answer:
                new_user_scores[user.id] =\
                    new_user_scores.get(user.id, 0) + 1

            # Give extra scores for users who submitted answer early regardless
            # of the answer is correct or not
            new_user_extra_scores[user.id] =\
                new_user_extra_scores.get(user.id, 0) + cur_extra

            cur_extra = max(cur_extra//2, 0)

    for user in User.objects.all():
        user.score = new_user_scores.get(user.id, 0)
        user.extra_score = new_user_extra_scores.get(user.id, 0)
        user.save()
