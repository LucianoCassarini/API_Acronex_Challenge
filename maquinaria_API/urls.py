from django.urls import path
from maquinaria_API.views import MaquinaView, MaquinaDetailView, ultimoPuntoConocido, AdminBajas
urlpatterns = [
    path('maquinaria/', MaquinaView.as_view(), name='maquinaria_list'),
    path('maquinaria/<int:id>/', MaquinaDetailView.as_view(), name='maquina_process'),
    path('maquinaria/ultimoPunto/<int:id>/', ultimoPuntoConocido),
    path('maquinaria/darDeBaja/<int:id>/', AdminBajas.as_view())
]