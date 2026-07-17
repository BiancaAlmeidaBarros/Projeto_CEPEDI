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
    path('diagnostico/', views.diagnostico, name="diagnostico"),
    path('historico_escolar/', views.historico_escolar, name="historico_escolar"),
    path('perfil_estudante/', views.perfil_estudante, name="perfil_estudante"),
    path("atividade/", views.atividade, name="atividade"),
    path("planejamento/", views.planejamento, name="planejamento"),
    path("habilidade_academica/", views.habilidade_academica, name="habilidade_academica"),
    path("adaptacao_curriculo/", views.adaptacao_curriculo, name="adaptacao_curriculo"),
    path("adaptacao_objetivo/", views.adaptacao_objetivo, name="adaptacao_objetivo"),
    path("adaptacao_conteudo/", views.adaptacao_conteudo, name="adaptacao_conteudo"),
    path("adaptacao_metodo/", views.adaptacao_metodo, name="adaptacao_metodo"),
    path("adaptacao_sistema/", views.adaptacao_sistema, name="adaptacao_sistema"),
    path("adaptacao_temporalidade/", views.adaptacao_temporalidade, name="adaptacao_temporalidade"),
    path("gerar_pdf/", views.gerar_pdf, name="gerar_pdf"),
    path("login/", views.login, name="login"),
    path("sair/", views.sair, name="sair"),
    path("painel_administrador/", views.painel_administrador, name="painel_administrador"),
    path("estudante_cadastrado/", views.estudante_cadastrado, name="estudante_cadastrado"),
    path("remover_estudante/", views.remover_estudante, name="remover_estudante"),
    path("remover_professor/", views.remover_professor, name="remover_professor"),
    path("remover_funcionario/", views.remover_funcionario, name="remover_funcionario"),
    path("professor_cadastrado/", views.professor_cadastrado, name="professor_cadastrado"),
    path("funcionario_cadastrado/", views.funcionario_cadastrado, name="funcionario_cadastrado"),
    path("gerenciar_professor/", views.gerenciar_professor, name="gerenciar_professor"),
    path("gerenciar_funcionario/", views.gerenciar_funcionario, name="gerenciar_funcionario"),
    path("gerenciar_estudante/", views.gerenciar_estudante, name="gerenciar_estudante"),
    path("cadastrar_pei/", views.cadastrar_pei, name="cadastrar_pei")
]

