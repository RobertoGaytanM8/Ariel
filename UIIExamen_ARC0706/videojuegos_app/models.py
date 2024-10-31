from django.db import models

# Create your models here.
class Videojuego(models.Model):
    Id=models.CharField(primary_key=True,max_length=6)
    Titulo=models.CharField(max_length=100)
    Genero=models.CharField(max_length=20)
    Plataforma=models.CharField(max_length=30)
    Fecha_lanzamiento=models.DateField()
    Stock=models.IntegerField()

    def __str__(self) -> str:
        return self.Titulo