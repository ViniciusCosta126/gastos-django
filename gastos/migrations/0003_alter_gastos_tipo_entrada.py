# Generated by Django 4.2.5 on 2023-09-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0002_gastos_valor_despesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='tipo_entrada',
            field=models.CharField(choices=[('D', 'Despesa'), ('G', 'Ganho')], default='D', max_length=1),
        ),
    ]
