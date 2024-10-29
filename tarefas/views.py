from django.shortcuts import render
from .models import Tarefa
# Create your views here.

from django.shortcuts import render
def lista_tarefas(request):
  tarefas = Tarefa.objects.all()
  return render(request, 'lista_tarefas.html', {'tarefas':
  tarefas})

