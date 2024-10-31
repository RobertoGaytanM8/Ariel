from django.shortcuts import render
from .models import Videojuego

# Create your views here.
def listadoVideojuego(request):
    elVideojuego=Videojuego.objects.all()
    return render(request,"gestonarVideojuegos.html",{"mivideojuego":elVideojuego})
