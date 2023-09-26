from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gastos
from datetime import datetime


def Home(request):
    data_param = request.GET.get('data')
    if data_param:
        novaData = data_param.split('/')
        gastos = Gastos.objects.filter(data_entrada__month=novaData[0])
        gastos = gastos.filter(data_entrada__year=novaData[1])
        data_formatada = f'{novaData[0]}/{novaData[1]}'

        if (int(novaData[0]) < 10):
            data_formatada = f'0{novaData[0]}/{novaData[1]}'
        return render(request, 'home.html', {'gastos': gastos, 'data': data_formatada})
    else:
        agora = datetime.today()
        data_formatada = f'{agora.month}/{agora.year}'
        if (agora.month < 10):
            data_formatada = f'0{agora.month}/{agora.year}'
        gastos = Gastos.objects.filter(data_entrada__month=agora.month)
        return render(request, 'home.html', {'gastos': gastos, 'data': data_formatada})


def AdicionarGasto(request):
    if (request.method == 'POST'):
        titulo = request.POST['title']
        data = request.POST['date']
        tipo = request.POST['tipo']
        valor = request.POST['valor']
        new_gasto = Gastos(titulo_entrada=titulo, tipo_entrada=tipo,
                           data_entrada=data, valor_despesa=valor)
        new_gasto.save()
        return redirect('add-gasto')
    return render(request, 'add-custo.html')


def EditarGasto(request, id):
    gasto = Gastos.objects.get(pk=id)
    if (gasto):
        gasto.valor_despesa = str(gasto.valor_despesa).replace(',', '.')

        if (request.method == "POST"):
            gasto.titulo_entrada = request.POST['title']
            gasto.tipo_entrada = request.POST['tipo']
            gasto.data_entrada = request.POST['date']
            gasto.valor_despesa = request.POST['valor']
            gasto.save()
            return redirect('home')

        return render(request, 'editar.html', {'gasto': gasto})


def DeletarGasto(request, id):
    if (request.method == 'GET'):
        gasto = Gastos.objects.filter(id=id)
        gasto.delete()

    return redirect('home')
