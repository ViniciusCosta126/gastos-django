from django.db import models

class Gastos(models.Model):
    TIPOS = [
        ("D", "Despesa"),
        ("G", "Ganho")
    ]
    titulo_entrada = models.CharField(max_length=100, blank=False, null=False)
    tipo_entrada = models.CharField(max_length=1,choices=TIPOS, default="D")
    data_entrada = models.DateField(blank=False,null=False)
    valor_despesa = models.DecimalField(decimal_places=2, default=0,max_digits=20)
    
    def __str__(self):
        return self.titulo_entrada

