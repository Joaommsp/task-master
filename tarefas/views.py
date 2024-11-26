from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarefa

@login_required
def lista_tarefas(request):
    if request.method == 'POST':
        if 'titulo-tarefa' in request.POST:
            # Adicionar nova tarefa
            titulo = request.POST.get('titulo-tarefa')
            descricao = request.POST.get('descricao-tarefa', '')
            concluida = request.POST.get('concluida') == 'on'

            if titulo:
                Tarefa.objects.create(titulo=titulo, descricao=descricao, concluida=concluida, usuario=request.user)

        elif 'editar-tarefa-id' in request.POST:
            # Editar tarefa
            tarefa_id = request.POST.get('editar-tarefa-id')
            tarefa = get_object_or_404(Tarefa, id=tarefa_id)

            tarefa.titulo = request.POST.get('editar-titulo', tarefa.titulo)
            tarefa.descricao = request.POST.get('editar-descricao', tarefa.descricao)
            tarefa.concluida = request.POST.get('editar-concluida') == 'on'
            tarefa.save()

        elif 'excluir-tarefa' in request.POST:
            # Excluir tarefa
            tarefa_id = request.POST.get('excluir-tarefa')
            Tarefa.objects.filter(id=tarefa_id).delete()

        elif 'concluir-tarefa' in request.POST:
            # Marcar como concluída
            tarefa_id = request.POST.get('concluir-tarefa')
            tarefa = get_object_or_404(Tarefa, id=tarefa_id)
            tarefa.concluida = True
            tarefa.save()

        return redirect('lista_tarefas')   

    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
