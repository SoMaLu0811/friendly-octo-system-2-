#Modelo de registro e configuração de Passaporte do usuário
from meuapp.models.base import basemodel
from meuapp.models.person import Person
from django.db import models
class Passport(basemodel):
    number=models.CharField(max_length=10,verbose_name='passaporte',help_text='Insira seu número de passaporte')
    issue_date=models.DateField(verbose_name='Issue_date',help_text='Insira sua data de expedição')
    expiration_date=models.DateField(verbose_name='Data de validade',help_text='Insira a sua data de validade do seu passaporte')
    person=models.OneToOneField(Person,on_delete=models.CASCADE, primary_key=True)
    class meta:
        abstract=False
    def issue_passport(self,issue_date,expiration_date):
        #TODO: implementar issue_date
        pass
   
        