#Modelo de registro de pessoa física
from meuapp.models.base import basemodel
from django.db import models
class Person(basemodel):
    name=models.CharField(max_length=100, verbose_name='Nome',help_text='Insira seu nome')
    birth_date=models.DateField(verbose_name='data de nascimento',help_text='Insira sua data de nascimento')
    cpf=models.CharField(max_length=11,verbose_name='cpf',help_text='Insira seu CPF')
    class Meta:
        abstract=False
    def checkvisa(self,place,data):
        #Fazer depois (verificação de visto do passaporte)
        pass
    def __str__(self):
        return self.name
    