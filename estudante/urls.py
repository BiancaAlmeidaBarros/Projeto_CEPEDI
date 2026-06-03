from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
    path('cadastro_sistema/', views.cadastro_sistema, name="cadastro_sistema"),
    path('cadastro_estudante/', views.cadastro_estudante, name="cadastro_estudante"),
    path('cadastro_professor/', views.cadastro_professor, name="cadastro_professor"),
    path('cadastro_funcionario/', views.cadastro_funcionario, name="cadastro_funcionario"),
    path('PEI/', views.pei, name="pei"),
    path('cadastro_equipe/', views.cadastro_equipe, name="cadastro_equipe"),
    path('diagnostico', views.diagnostico, name="diagnostico"),
]

