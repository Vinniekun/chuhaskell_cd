# # -*- coding: utf-8 -*-

from django import forms

from sensor.models import *
from localflavor.br.forms import BRStateChoiceField, BRZipCodeField


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


# class EstadoForm(BaseForm):
#     nome = BRStateChoiceField()
#
#     class Meta:
#         model = Estados
#         fields = '__all__'
#
#
# class MunicioForm(BaseForm):
#     class Meta:
#         model = Municipios
#         fields = '__all__'
#
#
class LocalForm(BaseForm):
    # cep = BRZipCodeField(label='CEP')

    class Meta:
        model = Local
        fields = '__all__'

class SensorForm(BaseForm):
    class Meta:
        model = Sensor
        fields = '__all__'


# class BlocoForm(BaseForm):
#     class Meta:
#         model = Blocos
#         fields = ['descricao']
#
#     def __init__(self, *args, **kwargs):
#         self.pk = kwargs.pop('pk', None)
#         super(BlocoForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = field.label
#
#     def save(self, commit=True):
#         instance = super(BlocoForm, self).save(commit=False)
#         instance.id_local_id = int(self.pk)
#         if commit:
#             instance.save()
#         return instance
#
#
# class AndarForm(BaseForm):
#     class Meta:
#         model = Andares
#         fields = ['descricao']
#
#     def __init__(self, *args, **kwargs):
#         self.pk = kwargs.pop('pk', None)
#         super(AndarForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = field.label
#
#     def save(self, commit=True):
#         instance = super(AndarForm, self).save(commit=False)
#         instance.id_bloco_id = int(self.pk)
#         if commit:
#             instance.save()
#         return instance
#
#
# class SetorForm(BaseForm):
#     class Meta:
#         model = Setores
#         fields = ['descricao']
#
#     def __init__(self, *args, **kwargs):
#         self.pk = kwargs.pop('pk', None)
#         super(SetorForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = field.label
#
#     def save(self, commit=True):
#         instance = super(SetorForm, self).save(commit=False)
#         instance.id_andar_id = int(self.pk)
#         if commit:
#             instance.save()
#         return instance
#
#
# class SecaoForm(BaseForm):
#     class Meta:
#         model = Secoes
#         exclude = ['id_setor']
#
#     def __init__(self, *args, **kwargs):
#         self.pk = kwargs.pop('pk', None)
#         super(SecaoForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = field.label
#
#     def save(self, commit=True):
#         instance = super(SecaoForm, self).save(commit=False)
#         instance.id_setor_id = int(self.pk)
#         if commit:
#             instance.save()
#         return instance
