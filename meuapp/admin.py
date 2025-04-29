from django.contrib import admin
from meuapp.models.account import account
from meuapp.models.person import Person 
from meuapp.models.passport import Passport
from meuapp.models.reporter import Reporter
from meuapp.models.article import Article
from meuapp.models.magazine import Magazine
admin.site.register(account)
admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Magazine)

