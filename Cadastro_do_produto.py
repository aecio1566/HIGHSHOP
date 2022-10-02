#CODIGO PROGRAMAÇÃO BECK END
import os
import time as t
from turtle import clear
import datetime

def clear_console():
    os.system("cls")


cadastro_geral = list()
cadastro = dict()
hoje = datetime.date.today()
while True:
    cadastro.clear
    #pagina de cadastro
    cadastro["tipo_evento"] = str(input("Qual o produto deseja cadastrar [X] Calcados [Y] Parte superior [Z] Parte inferior.\n")).upper()[0]
    while True:
        if cadastro["tipo_evento"] == 'X':
            print('Opcao cadstrada: Calcadaos')
            print('-'*30)
            break
        
        elif cadastro["tipo_evento"] == 'Y':
            print('Opcao cadastrada: Parte superior')
            print('-'*30)
            break
        
        elif cadastro["tipo_evento"] == 'Z':
            print("Opcao cadastrada como: Parte inferior")
            print('-'*30)
            break
        
        else:
            print("Opção indisponível!")
            break
    
    cadastro["nome"] = str(input("Qual o nome do produto\n"))
    cadastro["local"] = str(input("Qual estado do produto?\n"))
    
    #Opçao de drop:
    cadastro['resp']= str(input("Deseja criar um drop para seu produto? [S/N]\n" )).upper()[0]
    
    while True:
        if cadastro['resp'] == 'S':
            cadastro['resp'] = str(input('Qual a forma de contato com os clientes, e-mail[M] ou  NUMERO[NUM]\n')).upper()[0]
            
            if cadastro['resp'] == 'M':
                cadastro['resp']=  str(input("Insira seu email:\n"))
            
            elif cadastro['resp'] == 'NUM':
                cadastro['resp']  = str(input("Insira seu numero para contato:\n"))
            
            else:
                print("Opção indisponível!")
            
            drop = 's'
            
            cadastro["horario"] = int(input("Ate que horas vai o seu drop?\n"))
            
            break
        
        elif cadastro['resp'] == 'N':
            drop = 'n'
            break
        
        else:
            print("Opção indisponível!")
            break

    cadastro["data"] = input("informe ate que data o produto vai estar disponivel: (use o formato dd/mm/AAAA)\n")
    y = cadastro["data"].split('/')
    
    while True:
        cadastro['drop'] = str(input("Vai precisar de alguma ajuda?(Se sim, entraremos em contato) [S/N]\n")).upper()
        
        if cadastro['drop'] in "SN":
            break
        
        else:
            print("ERRO! Insira apenas [S/N]\n ")
    
    cadastro_geral.append(cadastro.copy())
    
    while True:
        
        if drop == 's':
            print("Seu produto foi cadastrado com sucesso!\n")
            final = str(input("Deseja cadastrar outro produto? [S/N]\n")).upper()
            if final in 'SN':
                if final == 'N':
                    print('-' * 30)
                    print(f"O seu produto foi classificado como: {cadastro['tipo_evento']} \n")
                    print('-' * 30)
                    print(f"O produto foi cadastrada como: {cadastro['nome']}\n") 
                    print('-' * 30)
                    print(f"O estado do produto cadastro foi: {cadastro['local']}\n")
                    print('-' * 30)
                    print(f"O Horário limite para as vendas foi: {cadastro['horario']} 'horas'\n")
                    print('-' * 30)
                    print(f"A data de cadastro foi:{y}\n")
                    print('-' * 30)
                    
                    t.sleep(5)
                    clear_console()
                    
                    print("\nEncerrando sessção...")
                    t.sleep(2)
                    clear_console()
                    print("Sessão encerrada!")
                    exit()
            
                else:
                    print('-' * 30)
                    print(f"O seu produto foi classificado como: {cadastro['tipo_evento']} \n")
                    print('-' * 30)
                    print(f"O produto foi cadastrada como: {cadastro['nome']}\n") 
                    print('-' * 30)
                    print(f"O estado do produto cadastro foi: {cadastro['local']}\n")
                    print('-' * 30)
                    print(f"O Horário limite para as vendas foi: {cadastro['horario']} 'horas'\n")
                    print('-' * 30)
                    print(f"A data de cadastro foi:{y}\n")
                    print('-' * 30)
                    
                    t.sleep(5)
                    clear_console()
                    print("Iniciando o cadastro do novo produto...\n")
                    break
                
            else:
                print("ERRO! digite apeans [S/N] n!\n")
        
        elif drop == 'n':
            print("Seu produto foi cadastrado com sucesso!\n")
            final = str(input("Deseja cadastrar outro produto? [S/N]\n")).upper()
            if final in 'SN':
                if final == 'N':
                    print('-' * 30)
                    print(f"O seu produto foi classificado como: {cadastro['tipo_evento']} \n")
                    print('-' * 30)
                    print(f"O produto foi cadastrada como: {cadastro['nome']}\n") 
                    print('-' * 30)
                    print(f"O estado do produto cadastro foi: {cadastro['local']}\n")
                    print('-' * 30)
                    print(f"A data de cadastro foi:{y}\n")
                    print('-' * 30)
                    
                    t.sleep(5)
                    clear_console()
                    
                    print("\nEncerrando sessção...")
                    t.sleep(2)
                    clear_console()
                    print("Sessão encerrada!")
                    exit()
            
                else:
                    print('-' * 30)
                    print(f"O seu produto foi classificado como: {cadastro['tipo_evento']} \n")
                    print('-' * 30)
                    print(f"O produto foi cadastrada como: {cadastro['nome']}\n") 
                    print('-' * 30)
                    print(f"O estado do produto cadastro foi: {cadastro['local']}\n")
                    print('-' * 30)
                    print(f"A data de cadastro foi:{y}\n")
                    print('-' * 30)
                    
                    t.sleep(5)
                    clear_console()
                    print("Iniciando o cadastro do novo produto...\n")
                    break
