from django.contrib import admin
from .models import Gastos

class ListandoGasto(admin.ModelAdmin):
    list_display=['titulo_entrada','tipo_entrada', 'data_entrada','valor_despesa']

admin.site.register(Gastos,ListandoGasto)