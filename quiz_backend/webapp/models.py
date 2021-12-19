from django.db import models

from utils import repr_common


class User(models.Model):
    name = models.CharField(max_length=512, unique=True)
    email = models.EmailField()
    score = models.IntegerField(default=0)

    def __repr__(self):
        return repr_common(self, ['name', 'email', 'score',])

    def __str__(self):
        return self.name


class Question(models.Model):
    CORRECT_ANSWER_O, CORRECT_ANSWER_X = 'o', 'x'
    CORRECT_ANSWER_CHOICES = [
        (CORRECT_ANSWER_O, 'o'),
        (CORRECT_ANSWER_X, 'x')
    ]
    number = models.IntegerField(unique=True, db_index=True)
    question = models.TextField(default='')
    correct_answer = models.CharField(max_length=1, choices=CORRECT_ANSWER_CHOICES)
    explanation = models.TextField(default='')

    class Meta:
        ordering = ['number']

    def __repr__(self):
        return repr_common(self, ['number', 'question'])

    def __str__(self):
        return self.question


class Answer(models.Model):
    SELECTION_O, SELECTION_X = 'o', 'x'
    SELECTION_CHOICES = [
        (SELECTION_O, 'o'),
        (SELECTION_X, 'x')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selection = models.CharField(max_length=1, choices=SELECTION_CHOICES)
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['user', 'question']]

    def __repr__(self):
        return repr_common(self, ['user', 'question', 'selection', 'datetime'])

    def __str__(self):
        return repr(self)
