from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserAdminCreationForm, UserUpdate

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'cpf', 'password1', 'password2')
        }),
    )
    form = UserUpdate
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'cpf')
        }),
        ('Informações Básicas', {
            'fields': ('nome', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'nome', 'email', 'is_active', 'is_staff', 'date_joined']

admin.site.register(User, UserAdmin)