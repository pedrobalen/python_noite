import os
import sys
from participante import *

lista_inscritos = []
def adicionar_inscricao(lista):
    matricula = input("Insira sua matricula: ")
    if matricula in lista:
        print("Matricula ja registrada no evento")
    else:
        lista.append(matricula)
        nome = input("Insira nome: ")    
        email = input("Insira email: ")
        email = email.lower()
        escritor = open('inscricoes.dat', 'a')
        escritor.write(matricula + ';' + nome + ';' + email)
        escritor.close()

                


def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0])
        leitor.close()
    except:
        pass

conexao_base(lista_inscritos)
while True:
    print("1 - Inscricao")
    print("2 - Listar Inscritos")
    print("3 - Registrar entrada")
    print("4 - Registrar saida")
    print("5 - Finalizar")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_inscricao(lista_inscritos)
    elif opcao == "2":
        listar_inscritos()
    elif opcao == "3":
        registar_entrada()
    elif opcao == "4":
        registrar_saida()       
    elif opcao == "5":
        sys.exit()    
    else:
        print("Opção inválida. Tente novamente.")
    
