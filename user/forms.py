from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from .models import User
from localflavor.br.forms import BRCPFField


# PLATAFORMA
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'nome', 'dir_imagem', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserCreation(UserCreationForm):
    cpf = BRCPFField(label='CPF')

    class Meta:
        model = User
        fields = ['username', 'nome', 'email', 'cpf']

    def __init__(self, *args, **kwargs):
        super(UserCreation, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_superuser', 'is_active']

    def __init__(self, *args, **kwargs):
        super(UserUpdate, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class PasswordForm(AdminPasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


# ADMIN
class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'nome', 'email', 'cpf']

    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'nome', 'is_active', 'is_staff']

    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
