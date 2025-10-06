from django.contrib import admin
from .models import Pessoa, Endereco

# Register your models here.
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('get_nome_completo', 'get_email_usuario', 'cpf', 'telefone')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'usuario__username', 'cpf')

    @admin.display(description='Nome Completo', ordering='usuario__first_name')
    def get_nome_completo(self, obj):
        return obj.usuario.get_full_name()
    
    @admin.display(description='E-mail', ordering='usuario__email')
    def get_email_usuario(self, obj):
        return obj.usuario.email

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'pais')
    search_fields = ('pessoa__usuario__username', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'pais')