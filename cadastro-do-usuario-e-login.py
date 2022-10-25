import os
import time


def clear_console():
    os.system('cls')
    
def delayed_clear_console(n):
    time.sleep(n)
    clear_console()

def cadastroCliente():
    while True:
        email = input("Digite o e-mail que deseja cadastrar: ")
        senha = input("Digite a senha que deseja cadastrar: ")
        senhav = input("Digite a senha novamente: ")
        
        while senha != senhav:
            senhav = input("A senha não corresponde! Digite novamente: ")
            
        clear_console()
        
        emailsenha = f"{email}{senha}"
        
        f = open("cadastroscliente.txt", "a")
        f.close()
        
        f = open("cadastroscliente.txt", "r")
        a = f.read()
        f.close()
        
        if emailsenha in a:
            cadastrar1 = input("Esse email já está cadastrado!\n\nDeseja realizar o login [s/n]").lower()
            if cadastrar1 == 's':
                login()
            
            else:
                while cadastrar1 not in 'sn':
                    print("Formato não aceito!")
                    
                    delayed_clear_console(2)
                    
                    cadastrar1 = input("Deseja realizar o login [s/n]").lower()
                    clear_console()
        
        else:
            nome = input("Digite seu 1º nome: ")
            sobrenome = input("Digite seu(s) sobrenome(s): ")
            nomesobrenomeCe = f"{nome}{sobrenome}"
            nomesobrenomeSe = nomesobrenomeCe.replace(" ", "")
            
            id = input("Digite um nome de usuário [Não pode conter espaços, acentos ou caracteres especiais, excluindo [-_.]]: ")
            
            idade = input("Digite sua data de nascimento [dd/mm/aaaa]: ")
            idade = idade.replace("/", "")
            
            linhas = f"{id}/{emailsenha}/{nomesobrenomeSe}/{idade}\n"
            
            print(f"Cadastro realizado com sucesso!\nSeu id de cliente é: {id}")
            
            f = open("cadastroscliente.txt", "a")
            f.writelines(linhas)
            f.close()
            
            delayed_clear_console(2)
            exit()
            
def cadastroEmpresas():
    while True:
        email = input("Digite o e-mail que deseja cadastrar: ")
        senha = input("Digite a senha que deseja cadastrar: ")
        senhav = input("Digite a senha novamente: ")
        
        while senha != senhav:
            senhav = input("A senha não corresponde! Digite novamente: ")
            
        clear_console()
        
        emailsenha = f"{email}{senha}"
        
        f = open("cadastrosempresas.txt", "a")
        f.close()
        
        f = open("cadastrosempresas.txt", "r")
        a = f.read()
        f.close()
        
        if emailsenha in a:
            cadastrar1 = input("Esse email já está cadastrado!\n\nDeseja realizar o login [s/n]").lower()
            if cadastrar1 == 's':
                login()
            
            else:
                while cadastrar1 not in 'sn':
                    print("Formato não aceito!")
                    
                    delayed_clear_console(2)
                    
                    cadastrar1 = input("Deseja realizar o login [s/n]").lower()
                    clear_console()
        
        else:
            nomeempresa = input("Digite o nome da sua empresa: ")
            nomeempresaSe = nomeempresa.replace(" ", "")
            
            cnpj = input("Digite o CNPJ [apenas números]: ")
            
            endereco = input("Digite o endereço da sua empresa [rua, nº(apenas números), bairro]")
            endereco = endereco.replace(" ", "")
            
            linhas = f"{emailsenha}/{nomeempresaSe}/{endereco}/{cnpj}\n"
            
            print("Cadastro realizado com sucesso!")
            
            f = open("cadastrosempresas.txt", "a")
            f.writelines(linhas)
            f.close()
            
            delayed_clear_console(2)
            exit()

def login():
    while True:
        email = input("Email: ")
        senha = input("Senha: ")
        emailsenha = f"{email}{senha}"
        
        f = open("cadastroscliente.txt", "a")
        f.close()
        
        g = open("cadastrosempresas.txt", "a")
        g.close()
        
        f = open("cadastroscliente.txt", "r")
        g = open("cadastrosempresas.txt", "r")
        
        t = f.read()
        u = g.read()
        
        if emailsenha not in t or emailsenha not in u:
            f.close()
            g.close()
            
            f = open("cadastroscliente.txt", "r")
            g = open("cadastrosempresas.txt", "r")
            
            t = f.read()
            u = g.read()
            
            while True:
                clear_console()
                
                cadastrar = input("Login não reconhecido!\n\nDeseja se cadastrar [s/n]?\n").lower()
                
                if cadastrar == 'n':
                    email = input("\nEmail: ")
                    senha = input("Senha: ")
                    emailsenha = f"{email}{senha}"
                
                elif cadastrar == 's':
                    clienteempresa = input("""
Digite:
- [c] Para se cadastrar como cliente
- [e] Para se cadastrar como empresa
""").lower()
                if clienteempresa == 'c':
                    cadastroCliente()
                
                else:
                    clear_console()
                    print("\nFormato não aceito!")
                    
                    delayed_clear_console(2)
                
                f.close()
                g.close()
                
                f = open("cadastroscliente.txt", "r")
                g = open("cadastrosempresas.txt", "r")
                
                t = f.read()
                u = g.read()
                
                if emailsenha in t or emailsenha in u:
                    break
        
        f.close()
        g.close()
        clear_console()
        print("Login realizado com sucesso!")
        delayed_clear_console(2)
        exit()
    


while True:
    cadastrado = input("Você já é cadastrado [s/n]?\n").lower()
    
    if cadastrado == 'n':
        clienteempresa = input("""
Digite:
- [c] Para se cadastrar como cliente
- [e] Para se cadastrar como empresa
""").lower()
        
        if clienteempresa == 'c':
            cadastroCliente()
        
        elif clienteempresa == 'e':
            cadastroEmpresas()
        
        else:
            while clienteempresa not in 'ce':
                clear_console()
                print("Formato não aceito!\nDigite apenas [c] ou [e]")
                delayed_clear_console()
                clienteempresa = input("""
Digite:
- [c] Para se cadastrar como cliente
- [e] Para se cadastrar como empresa
""").lower()
                
                
        

    elif cadastrado == 's':
        login()

    else:
        print("Formato não aceito!")
        delayed_clear_console(2)
