from django.contrib import admin
from projetos.models import Projeto
# Register your models here.

class ProjetoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Projeto, ProjetoAdmin)