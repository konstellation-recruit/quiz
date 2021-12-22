def admin_default(
    cls, readonly=False, form=None, list_extra:list=None, list_exclude=(),
    readonly_fields=(), list_filter=(), ordering=(), raw_id_fields=()):

    fields = [
        field.name for field in cls._meta.fields
        if field.name != 'id' and not field.name.endswith('_ptr')]

    _list_display = fields
    if list_exclude:
        _list_display = [field for field in fields if field not in list_exclude]
    if list_extra:
        _list_display.extend(list_extra)

    from django.contrib import admin
    class Admin(admin.ModelAdmin):
        list_display = ['id'] + _list_display

    if readonly:
        assert not readonly_fields
        Admin.readonly_fields = fields
    elif readonly_fields:
        Admin.readonly_fields = readonly_fields

    Admin.fields = fields

    for option_name, option in [
        ('readonly_fields', readonly_fields),
        ('list_filter', list_filter), ('ordering', ordering),
        ('form', form), ('raw_id_fields', raw_id_fields)]:

        if option:
            setattr(Admin, option_name, option)

    admin.site.register(cls, Admin)


def repr_common(self, fields, custom:dict=None):
    class_name = self.__class__.__name__
    args = []
    for field in fields:
        rp = repr(getattr(self, field))
        arg = f'{field}={rp}'
        args.append(arg)
    if custom:
        for key, val in custom.items():
            arg = f'{key}={val}'
            args.append(arg)

    return f'{class_name}({", ".join(args)})'


def update_scores():
    """
    This function is dumb in a sense that it will repeat iterating the
    same question assuming you will call this several time. But the computation
    will be trivial enough and it gaurantess the sum is correct, so we will
    stick with dum implementation.
    """
    from .models import User, Question

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
