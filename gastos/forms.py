from django.forms import ModelForm
from .models import Gastos

class GastoForm(ModelForm):
    class Meta:
        model = Gastos
        fields = ['titulo_entrada','tipo_entrada','data_entrada','valor_despesa']