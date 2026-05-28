import json

from django.core.handlers.base import reset_urlconf
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import SistemaProfessor, Estudante, Professor, Funcionario
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
        professor = SistemaProfessor.objects.filter(cpf=cpf)
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
        estudante = Estudante.objects.filter(cpf=cpf)
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
        professor = Professor.objects.filter(cpf=cpf)
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
        funcionario = Funcionario.objects.filter(cpf=cpf)
        if funcionario:
            return HttpResponse("Funcionario cadastrado ")
        else:
            return  HttpResponse("Funcionario não cadastrado")

def pei(request):
    if request.method == "GET":
        quantidade = request.GET.get("quantidade", 0)
        quantidade = int(quantidade)
        lista = range(quantidade)
        dicionario = {"quantidade":quantidade, "lista":lista}
        return render(request, 'PEI.html', dicionario)
    elif request.method == "POST":
        matricula_estudante = request.POST.get("matricula_estudante")
        matricula_professor = request.POST.get("matricula_professor")
        quantidade = request.GET.get("quantidade", 0)
        quantidade = int(quantidade)
        lista = range(quantidade)
        lista_funcionario = []
        for i in lista:
            funcionario = request.POST.get(f"cpf_{i}")
            lista_funcionario.append(funcionario)
        dicionario = {"matricula_estudante":matricula_estudante,
                      "matricula_professor":matricula_professor,
                      "lista_funcionario":lista_funcionario}
        return HttpResponse(json.dumps(dicionario))