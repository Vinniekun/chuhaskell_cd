from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import *

from user.forms import *
from django.contrib.messages.views import SuccessMessageMixin

from .forms import *
from sensor.models import *

# password
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.urls import reverse_lazy

@staff_member_required
def index(request):
    return render(request, 'adm/index.html', {'countUsuarios': User.objects.all().count(),
                                              'countLocais': Local.objects.all().count(),
                                              'countSensores': Sensor.objects.all().count()})

# USUARIOS
@staff_member_required
def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'adm/usuarios.html', {'usuarios': usuarios})


@method_decorator(staff_member_required, name='dispatch')
class AddUser(SuccessMessageMixin, CreateView):
    model = User
    success_url = '/'
    template_name = 'adm/crud.html'
    form_class = UserCreation
    success_message = 'Usuario criado'
    extra_context = {'title': 'Adicionar Usuário'}

    # def get_success_url(self):
    #     pass


@method_decorator(staff_member_required, name='dispatch')
class UserUpdate(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'adm/crud.html'
    success_message = 'Usuário Atualizado'
    form_class = UserUpdate
    success_url = '/adm/usuarios'
    extra_context = {'title': 'Editar Usuário'}


@method_decorator(staff_member_required, name='dispatch')
class UserDelete(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('adm:usuarios')
    success_message = 'Usuário Deletado'
    template_name = 'adm/confirm_delete.html'


@staff_member_required
def user_change_password(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = PasswordForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha trocada com sucesso!')
            return redirect('adm:edituser', pk=user.id)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'adm/crud.html', {
        'form': form,
        'title': 'Trocar senha ' + user.username
    })
############################


# Local
@staff_member_required
def locais(request):
    locais = Local.objects.all()
    context = {
        'locais': locais,
    }
    return render(request, 'adm/locais.html', context)


@method_decorator(staff_member_required, name='dispatch')
class AddLocal(SuccessMessageMixin, CreateView):
    model = Local
    form_class = LocalForm
    template_name = 'adm/crud.html'
    success_message = 'Local Adicionada'
    success_url = '/adm/locais'
    extra_context = {'title': 'Adicionar Local'}

    # def get_success_url(self):
    #     pass

@method_decorator(staff_member_required, name='dispatch')
class LocalUpdate(SuccessMessageMixin, UpdateView):
    model = Local
    form_class = LocalForm
    template_name = 'adm/crud.html'
    success_url = '/adm/locais'
    success_message = 'Local Atualizado'
    extra_context = {'title': 'Editar Local'}


@method_decorator(staff_member_required, name='dispatch')
class LocalDelete(SuccessMessageMixin, DeleteView):
    model = Local
    success_url = reverse_lazy('adm:locais')
    success_message = 'Local Deletado'
    template_name = 'adm/confirm_delete.html'


############################
@staff_member_required
def sensores(request):
    sensores = Sensor.objects.all()
    context = {
        'sensores': sensores,
    }
    return render(request, 'adm/sensores.html', context)


@method_decorator(staff_member_required, name='dispatch')
class AddSensor(SuccessMessageMixin, CreateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'adm/crud.html'
    success_message = 'Sensor Adicionada'
    extra_context = {'title': 'Adicionar Sensor'}
    success_url = '/adm/sensores'

    # def get_success_url(self):
    #     pass

@method_decorator(staff_member_required, name='dispatch')
class SensorUpdate(SuccessMessageMixin, UpdateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'adm/crud.html'
    success_message = 'Sensor Atualizado'
    extra_context = {'title': 'Editar Sensor'}
    success_url = '/adm/sensores'


@method_decorator(staff_member_required, name='dispatch')
class SensorDelete(SuccessMessageMixin, DeleteView):
    model = Sensor
    success_url = reverse_lazy('adm:Sensor')
    success_message = 'Sensor Deletado'
    template_name = 'adm/confirm_delete.html'


############################





