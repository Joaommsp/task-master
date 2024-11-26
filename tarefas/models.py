from django.contrib.auth.models import User, models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo