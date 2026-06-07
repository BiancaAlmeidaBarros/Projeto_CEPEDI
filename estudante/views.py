import json

from django.core.handlers.base import reset_urlconf
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import (SistemaProfessor, Estudante, Professor, Funcionario, PEI,
                     FuncionarioEstudante, Diagnostico, HistoricoEscolar,
                     PerfilEstudante, Atividade, Planejamento)
# Create your views here.

def cadastro(request):
    return render(request, 'index.html')

def cadastro_sistema(request):
    if request.method == "GET":
        return render(request, 'sistema_cadastro.html')
    elif request.method == "POST":
        cpf  = request.POST.get("cpf")
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        SistemaProfessor.objects.create(cpf=cpf, nome=nome, email=email, senha=senha)
        professor = SistemaProfessor.objects.filter(cpf=cpf).first()
        if professor:
            return HttpResponse("o usuario foi cadastrado")
        else:
            return HttpResponse("o usuario não foi cadastrado")

def cadastro_estudante(request):
    if request.method == "GET":
        return render(request, 'cadastro_estudante.html')
    elif request.method == "POST":
        cpf = request.POST.get("cpf")
        matricula = request.POST.get("matricula")
        nome = request.POST.get("nome")
        data_de_nascimento = request.POST.get("data_de_nascimento")
        curso = request.POST.get("curso")
        periodo = request.POST.get("periodo")
        turma = request.POST.get("turma")
        ingresso = request.POST.get("ingresso")
        nota = request.POST.get("nota")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        pai = request.POST.get("pai")
        mae = request.POST.get("mae")
        telefone_responsavel = request.POST.get("telefone_responsavel")
        email_responsavel = request.POST.get("email_responsavel")
        Estudante.objects.create(cpf=cpf, matricula=matricula, nome=nome,
                                 data_de_nascimento=data_de_nascimento, curso=curso,
                                 periodo=periodo, turma=turma, ingresso = ingresso,
                                 nota=nota, telefone=telefone, email=email, pai=pai, mae=mae,
                                 telefone_responsavel=telefone_responsavel,
                                 email_responsavel=email_responsavel)
        estudante = Estudante.objects.filter(cpf=cpf).first()
        if estudante:
            return HttpResponse("estudante cadastrado ")
        else:
            return HttpResponse("estudante não cadastrado ")

def cadastro_professor(request):
    if request.method == "GET":
        return render(request, 'cadastro_professor.html')
    elif request.method == "POST":
        cpf = request.POST.get("cpf")
        nome = request.POST.get("nome")
        matricula = request.POST.get("matricula")
        data_de_nascimento = request.POST.get("data_de_nascimento")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        Professor.objects.create(cpf=cpf, nome=nome, matricula=matricula,
                                 data_de_nascimento=data_de_nascimento, email=email,
                                 telefone=telefone)
        professor = Professor.objects.filter(cpf=cpf).first()
        if professor:
            return HttpResponse("O professor foi cadastrado ")
        else:
            return HttpResponse("O professor não foi cadastrado ")

def cadastro_funcionario(request):
    if request.method == "GET":
        return render(request, 'cadastro_funcionario.html')
    elif request.method == "POST":
        cpf = request.POST.get("cpf")
        nome = request.POST.get("nome")
        funcao = request.POST.get("funcao")
        Funcionario.objects.create(cpf=cpf, nome=nome, funcao=funcao)
        funcionario = Funcionario.objects.filter(cpf=cpf).first()
        if funcionario:
            return HttpResponse("Funcionario cadastrado ")
        else:
            return  HttpResponse("Funcionario não cadastrado")

def pei(request):
    if request.method == "GET":
        return render(request, 'PEI.html')
    elif request.method == "POST":
        matricula_estudante = request.POST.get("matricula_estudante")
        matricula_professor = request.POST.get("matricula_professor")
        validade = request.POST.get("validade")
        estudante = Estudante.objects.filter(matricula = matricula_estudante).first()
        professor = Professor.objects.filter(matricula = matricula_professor).first()
        if estudante and professor:
            PEI.objects.create(estudante=estudante, professor=professor, tempo=validade)
            return HttpResponse("PEI cadastrado")
        else:
            return HttpResponse("PEI não cadastrado")

def cadastro_equipe(request):
    if request.method == "GET":
        quantidade = request.GET.get("quantidade", 0)
        quantidade = int(quantidade)
        lista = range(quantidade)
        dicionario = {"quantidade":quantidade, "lista":lista}
        return render(request, 'cadastro_equipe.html', dicionario)
    elif request.method == "POST":
        quantidade = request.POST.get("quantidade", 0)
        quantidade = int(quantidade)
        matricula = request.POST.get("matricula")
        estudante = Estudante.objects.filter(matricula=matricula).first()
        for i in range(quantidade):
            cpf = request.POST.get(f"cpf_{i}")
            funcionario = Funcionario.objects.filter(cpf=cpf).first()
            if estudante and funcionario:
                FuncionarioEstudante.objects.create(estudante=estudante, funcionario=funcionario)
            else:
                return HttpResponse("equipe não cadastrada")
        return HttpResponse("equipe cadastrada")

def diagnostico(request):
    if request.method == "GET":
        return render(request, 'diagnostico.html')
    elif request.method == "POST":
        estudante = request.POST.get("estudante")
        laudo = request.POST.get("laudo")
        texto_diagnostico = request.POST.get("texto_diagnostico")
        ano = request.POST.get("ano")
        ano = int(ano)
        atendimento = request.POST.get("atendimento")
        texto_atendimento = request.POST.get("texto_atendimento", " ")
        estudante = Estudante.objects.filter(matricula=estudante).first()
        if estudante:
            Diagnostico.objects.create(estudante=estudante, laudo=laudo,
                                       texto=texto_diagnostico, ano_diagnostico=ano,
                                       atendimento_fora_da_escola = atendimento,
                                       texto_atendimento=texto_atendimento)
            return HttpResponse("diagnostico cadastrado")
        return HttpResponse("diagnostico não cadastrado")

def historico_escolar(request):
    if request.method == "GET":
        return render(request, 'historico_escolar.html')
    elif request.method == "POST":
        matricula = request.POST.get("matricula")
        texto = request.POST.get("texto")
        texto2 = request.POST.get("texto2")
        estudante = Estudante.objects.filter(matricula=matricula).first()
        if estudante:
            HistoricoEscolar.objects.create(texto=texto, texto2=texto2, estudante=estudante)
            return HttpResponse("historico escolar cadastrado")
        return HttpResponse("historico escolar não cadastrado")

def perfil_estudante(request):
    if request.method == "GET":
        return render(request, 'perfil_estudante.html')
    elif request.method == "POST":
        matricula = request.POST.get("matricula")
        interesse = request.POST.get("interesse")
        habilidade = request.POST.get("habilidade")
        nao_gosta = request.POST.get("nao_gosta")
        desafio = request.POST.get("desafio")
        informacao = request.POST.get("informacao")
        estudante = Estudante.objects.filter(matricula=matricula).first()
        if estudante:
            PerfilEstudante.objects.create(estudante=estudante,
                                           interesse=interesse, habilidade = habilidade,
                                           nao_gosta=nao_gosta, dificuldade=desafio,
                                           informacao=informacao)
            return HttpResponse("perfil do estudante cadastrado")
        return HttpResponse("perfil do estudante não cadastrado")

def atividade(request):
    if request.method == "GET":
        return render(request, "atividade.html")
    elif request.method == "POST":
        matricula = request.POST.get("matricula")
        atividade1 = request.POST.get("atividade")
        descricao = request.POST.get("descricao")
        estudante = Estudante.objects.filter(matricula=matricula).first()
        if estudante:
            Atividade.objects.create(estudante=estudante, atividade=atividade1,
                                     descricao=descricao)
            return HttpResponse("Atividade cadastrada")
        return HttpResponse("Atividade não cadastrada")

def planejamento(request):
    if request.method == "GET":
        return render(request, "planejamento.html")
    elif request.method == "POST":
        matricula = request.POST.get("matricula")
        habilidade = request.POST.get("habilidade")
        metas_curto_prazo = request.POST.get("meta_curto_prazo")
        metas_medio_prazo = request.POST.get("meta_medio_prazo")
        metas_longo_prazo = request.POST.get("meta_longo_prazo")
        estudante = Estudante.objects.filter(matricula=matricula).first()
        if estudante:
            Planejamento.objects.create(estudante=estudante, habilidade=habilidade,
                                        metas_curto_prazo=metas_curto_prazo,
                                        metas_medio_prazo = metas_medio_prazo,
                                        metas_longo_prazo = metas_longo_prazo)
            return HttpResponse("Planejamento cadastrado")
        return HttpResponse("Planejamento não cadastrado")