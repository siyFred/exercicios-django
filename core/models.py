from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    # email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=100, default='Brasil')

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"