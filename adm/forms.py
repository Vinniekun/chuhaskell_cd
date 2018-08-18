# # -*- coding: utf-8 -*-

from django import forms

from sensor.models import *


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class LocalForm(BaseForm):

    class Meta:
        model = Local
        fields = '__all__'

class SensorForm(BaseForm):
    class Meta:
        model = Sensor
        fields = '__all__'


