#Formulário de contato para o usuário
from django import forms
class ContactForm(forms.Form):
    #Formulário não será salvo no banco de dados (Método forms)
    subject=forms.CharField(max_length=200,help_text='Insira o assunto da mensagem', label='Assunto do Email',initial='Contato')
    name=forms.CharField(max_length=200,label='Nome completo',help_text='Insira seu nome completo')
    email=forms.EmailField(max_length=100,label='Endereço de E-mail',help_text='Insira seu endereço de E-mail')
    copy=forms.BooleanField(required=False) #cópia da mensagem de contato
    message=forms.CharField(widget=forms.Textarea,help_text='Insira sua mensagem')
    