from meuapp.models.base import basemodel
from django.db import models
class Reporter(basemodel):
    name=models.CharField(max_length=100,verbose_name='Nome Completo',help_text="Insira seu nome completo")
    email=models.EmailField(verbose_name='E-mail',help_text="Insira seu E-mail")
    cpf=models.CharField(max_length=11,verbose_name='CPF',help_text="Insira seu número de cpf")
    class Meta:
        abstract=False
    def __str__(self):
        return self.name