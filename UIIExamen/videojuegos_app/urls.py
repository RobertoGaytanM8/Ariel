from django.urls import path
from videojuegos_app import views
urlpatterns = [
    path("",views.listadoVideojuego,name="listadoVideojuegos")
]