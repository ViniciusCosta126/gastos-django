from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gastos
from datetime import datetime
from .forms import GastoForm

def Home(request):
    data_param = request.GET.get('data')
    valor_total = 0
    if data_param:
        novaData = data_param.split('/')
        gastos = Gastos.objects.filter(data_entrada__month=novaData[0])
        gastos = gastos.filter(data_entrada__year=novaData[1])
        data_formatada = f'{novaData[0]}/{novaData[1]}'

        if (int(novaData[0]) < 10):
            data_formatada = f'0{novaData[0]}/{novaData[1]}'
        
        for gasto in gastos:
            if(gasto.tipo_entrada == "D"):
                valor_total-= gasto.valor_despesa
            else:
                valor_total+= gasto.valor_despesa
        return render(request, 'home.html', {'gastos': gastos, 'data': data_formatada,'total': valor_total})
    else:
        agora = datetime.today()
        data_formatada = f'{agora.month}/{agora.year}'
        if (agora.month < 10):
            data_formatada = f'0{agora.month}/{agora.year}'
        gastos = Gastos.objects.filter(data_entrada__month=agora.month)
        for gasto in gastos:
            if(gasto.tipo_entrada == "D"):
                valor_total-= gasto.valor_despesa
            else:
                valor_total+= gasto.valor_despesa

           
        return render(request, 'home.html', {'gastos': gastos, 'data': data_formatada,'total':valor_total})


def AdicionarGasto(request):
    if (request.method == 'POST'):
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            return redirect('add-gasto')
    
    form = GastoForm()
    return render(request, 'add-custo.html',{'form':form})


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
