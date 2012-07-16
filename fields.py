from django.forms import fields
from .widgets import FilePickerURLWidget
from django.db import models

#Change path of field in your app
from south.modelsinspector import add_introspection_rules  
add_introspection_rules([], ["^apps\.fields\.FilePickerURLModelField"])

class FilePickerURLField(fields.MultiValueField):
    widget = FilePickerURLWidget

    def __init__(self, *args, **kwargs):
        all_fields = (
                fields.URLField(),
                fields.CharField(),
                fields.CharField(),
                )
        super(FilePickerURLField, self).__init__(all_fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return ':::'.join(data_list)
        return ''

    def clean(self, value):
        return super(FilePickerURLField, self).clean(value)

class FilePickerURLModelField(models.Field):
    __metaclass__ = models.SubfieldBase

    def formfield(self, **kwargs):
        defaults = {'form_class': FilePickerURLField}
        defaults.update(kwargs)
        return super(FilePickerURLModelField, self).formfield(**defaults)

    def get_internal_type(self):
        return 'TextField'

    def get_prep_value(self, value):
        return ':::'.join(value)

    def to_python(self, value):
        if value:
            if isinstance(value, list):
                return value
            else:
                return value.split(':::')[0:3]
        return ['','',''] 
    



