#CODIGO PROGRAMAÇÃO BECK END
import os
from turtle import clear
import datetime


cadastro_geral = list()
cadastro = dict()
hoje = datetime.date.today()
while True:
    cadastro.clear
    #pagina de cadastro de produto e drops
    cadastro["tipo_produto"] = str(input("Qual o produto deseja cadastrar [X] Calcados [Y] Parte superior [Z] Parte inferior.\n")).upper()[0]
    while True:
        if cadastro["tipo_produto"] == 'X':
            print('Opcao cadstrada: Calcadaos')
            print('-'*30)
        if cadastro["tipo_produto"] == 'Y':
            print('Opcao cadastrada: Parte superior')
            print('-'*30)
        if cadastro["tipo_produto"] == 'Z':
              print("Opcao cadastrada como: Parte inferior")
              print('-'*30)          
        else: 
             break
    
    cadastro["nome"] = str(input("Qual o nome do produto\n"))
    cadastro["estado"] = str(input("Qual estado do produto?\n"))
    #Opçao de drop:
    cadastro['resp']= str(input("Deseja criar um drop para seu produto? [S/N]\n" )).upper()[0]
    
    while True:
        if cadastro['resp'] == 'S':
            cadastro['resp'] = str(input('Qual a forma de contato com os clientes, e-mail[M] ou  NUMERO[NUM]\n')).upper()[0]
        elif cadastro['resp'] == 'M':
           cadastro['resp']=  str(input("Insira seu email:\n"))
        elif cadastro['resp'] == 'NUM':
            cadastro['resp']  = str(input("Insira seu numero para contato:\n"))
        else:
            break

    cadastro["data"] = input("informe ate que data o produto vai estar disponivel: (use o formato dd/mm/AAAA)\n")
    
    y = cadastro["data"].split('/')
    cadastro["horario"] = int(input("Ate que horas vai o seu drop?\n"))
    while True:
        cadastro['drop'] = str(input("Vai precisar de alguma ajuda?(Se sim, entraremos em contato) [S/N]\n")).upper()
        if cadastro['drop'] in "SN":
            break
        print("ERRO! Insira apenas [S/N]\n ")
    cadastro_geral.append(cadastro.copy())   
    while True:
        print("Seu produto foi cadastrado com sucesso!\n")
        final = str(input("Deseja cadastrar outro produto? [S/N]\n")).upper()
        if final in 'SN':
            break
        print("ERRO! digite apeans [S/N] n!\n")  
    if final == 'N':
        break  

print('-' * 30)
print(f"O seu produto foi classificado como: {cadastro['tipo_produto']} \n")
print('-' * 30)
print(f"O produto foi cadastrada como: {cadastro['nome']}\n") 
print('-' * 30)
print(f"O estado do produto cadastro foi: {cadastro['estado']}\n")
print('-' * 30)
print(f"O Horário flimite para as vendas foi: {cadastro['horario']} 'horas'\n")
print('-' * 30)
print(f"A data de cadastro foi:{y}\n")
print('-' * 30)
 #print ("linha para voltar para a pagina inicial")
