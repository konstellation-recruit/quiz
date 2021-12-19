import os


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


# https://github.com/dancaron/Django-ORM/blob/master/main.py
# Django ORM Standalone Python Template
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

def init_django():
    # Avoid initializing twice
    if os.environ.get("DJANGO_SETTINGS_MODULE"):
        return
    # Turn off bytecode generation
    import sys
    # sys.dont_write_bytecode = True  # NOTE: is this needed?
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_backend.settings")
    import django
    django.setup()
