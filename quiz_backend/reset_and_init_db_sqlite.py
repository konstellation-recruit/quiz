# This is used to keep consistent DB entries across different dev environemnts in testing

import os
import subprocess

from global_utils import init_django
init_django()

from webapp.models import User, Question, Answer


RESET = True


def reset_db():
    dname = os.path.dirname(__file__)
    db_path = os.path.join(dname, 'db.sqlite3')
    if os.path.exists(db_path):
        os.remove(db_path)

    migrations_path = os.path.join(dname, 'webapp/migrations')
    fnames = os.listdir(migrations_path)

    # Remove 0001_init.py and the following migration files
    for fn in fnames:
        if fn.startswith('__'):
            continue
        path = os.path.join(migrations_path, fn)
        os.remove(path)

    subprocess.run("python3 manage.py makemigrations".split())
    subprocess.run("python3 manage.py migrate".split())
    print("\n*create a superuser with id: admin, pw: admin\n")
    os.environ.update({
        'DJANGO_SUPERUSER_USERNAME': 'admin',
        'DJANGO_SUPERUSER_PASSWORD': 'admin',
        'DJANGO_SUPERUSER_EMAIL': 'a@a.com'})
    subprocess.run(
        "python3 manage.py createsuperuser --noinput".split())


if RESET:
    reset_db()


users = [
    ('hoon', 'hoon@vegaxholdings.com'),
    ('chang', 'chang@vegaxholdings.com'),
    ('soo', 'soo@vegaxholdings.com'),
]

questions = [
    (
        1,
        'Elon Musk started Doge Coin project',
        Question.CORRECT_ANSWER_X,
        'No, he is only the father of the doge coin, not the creator.'
    ),
    (
        2,
        'Today is Sunday',
        Question.CORRECT_ANSWER_O,
        'Today is sunday and we are still in the office.'
    )
]

answers = [(1, 1, 'x'), (2, 1, 'x'), (3, 1, 'o')]

for name, email in users:
    u = User(name=name, email=email)
    u.save()
    print('added', u)
del name, email


for number, question, correct_answer, explanation in questions:
    q = Question(
        number=number,
        question=question,
        correct_answer=correct_answer,
        explanation=explanation
    )
    q.save()
    print('added', q)
del number, question, correct_answer, explanation


for user, question, selection in answers:
    a = Answer(
        user=User.objects.get(id=user),
        question=Question.objects.get(id=question),
        selection=selection
    )
    a.save()
    print('added', a)
