# Generated by Django 4.2.5 on 2023-09-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_entrada', models.CharField(max_length=100)),
                ('tipo_entrada', models.CharField(choices=[(1, 'Despesa'), (2, 'Ganho')], default=1, max_length=1)),
                ('data_entrada', models.DateField()),
            ],
        ),
    ]