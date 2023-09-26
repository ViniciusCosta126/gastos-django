from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Gastos


def Home(request):
    gastos = Gastos.objects.filter()
    return render(request, 'home.html', {'gastos': gastos})


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
