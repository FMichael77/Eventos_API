from django.db import models
  
  
class CategoriaEvento(models.Model):
    nome = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    
    
class Evento(models.Model):
    nome = models.CharField(max_length=200)
    capacidade = models.CharField(max_length=10)
    rua = models.CharField(max_length=80)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    categoria_evento = models.ForeignKey(CategoriaEvento, related_name='eventos', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='eventos', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('nome',)
    
    def __str__(self):
        return self.nome
    
    
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    rua = models.CharField(max_length=80)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    
    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    
    
class Comentario(models.Model):
    conteudo = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, related_name='comentarios', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('conteudo',)

    def __str__(self):
        return self.nome
 