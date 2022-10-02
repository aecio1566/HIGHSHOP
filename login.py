import os
import time

def clear_console():
    os.system('cls')
    
cadastrado = input("Você já é cadastrado [s/n]?\n")

while True:
    if cadastrado == 'n':
        while True:
            email = input("Digite o e-mail que deseja cadastrar: ")
            senha = input("Digite a senha que deseja cadastrar: ")
            senhav = input("Digite a senha novamente: ")
            
            while senha != senhav:
                senhav = input("A senha não corresponde! Digite novamente: ")
                
            clear_console()
                
            print("\n\nCadastro realizado com sucesso!")
            
            emailsenha = f"{email}{senha}"
            
            f = open("cadastros.txt", "a")
            f.writelines(emailsenha, "\n")
            f.close()
            break
        time.sleep(2)
        clear_console()
        exit()

    elif cadastrado == 's':
        while True:
            email = input("Email: ")
            senha = input("Senha: ")
            emailsenha = f"{email}{senha}"
            
            f = open("cadastros.txt", "r")
            
            if emailsenha not in f.read():
                while True:
                    clear_console()
                    print("Login não reconhecido!\n\nTente novamente!")
                    
                    email = input("\nEmail: ")
                    senha = input("Senha: ")
                    emailsenha = f"{email}{senha}"
                    
                    if emailsenha in f.read():
                        break
            
            f.close()
            clear_console()
            print("\n\nLogin realizado com sicesso!")
            time.sleep(2)
            clear_console()
            exit()

    else:
        print("Formato não aceito!")
        time.sleep(2)
        clear_console()
