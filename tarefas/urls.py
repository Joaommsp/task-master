from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
  path('login/', LoginView.as_view(), name='login'),
  path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
  path('', views.lista_tarefas, name='lista_tarefas'),
]
