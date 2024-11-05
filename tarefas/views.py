from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo-tarefa')
        descricao = request.POST.get('descricao-tarefa', '')
        concluida = request.POST.get('concluida') == 'on'
        
        if titulo:
            Tarefa.objects.create(titulo=titulo, descricao=descricao, concluida=concluida)
        return redirect('lista_tarefas')
    
    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
