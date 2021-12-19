import time

from utils import init_django

init_django()

from webapp.models import Question


def run_quiz():
    for q in Question.objects.all():
        print("start new question")
        print(q)
        print("receive answers from users realtime, redis")
        time.sleep(30)

        print("compute user scores and save them")


if __name__ == '__main__':
    run_quiz()
