from meuapp.models.base import basemodel
from django.contrib.auth.models import User
from django.db import models
class account(basemodel):
    owner=models.ManyToManyField(User, verbose_name='Conta')
    description=models.CharField(max_length=200, help_text='Descriça da sua conta')
    number=models.CharField(max_length=200,help_text='Insira o número da sua conta')
    balance=models.FloatField(default=0,help_text='Insira o seu saldo inicial')   
    class Meta:
        abstract=False
    def __str__(self):
        return f'{self.number}: {self.description} - {self.balance}:'
    def update_balance(self,value):
        try:
            self.balance+=float(value)
            return True
        except: return False
    def get_balance(self):
        return self.balance
    
        