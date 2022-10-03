import os
import time

def clear_console():
    os.system('cls')
    
cadastrado = input("Você já é cadastrado [s/n]?\n").lower()

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
            
            emailsenha = f"{email}{senha}\n"
            
            f = open("cadastros.txt", "a")
            f.writelines(emailsenha)
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
            
            t = f.read()
            
            if emailsenha not in t:
                f.close()
                f = open("cadastros.txt", "r")
                t = f.read()
                
                while True:
                    clear_console()
                    
                    cadastrar = input("Login não reconhecido!\n\nDeseja se cadastrar [s/n]?\n").lower()
                    
                    if cadastrar == 'n':
                        email = input("\nEmail: ")
                        senha = input("Senha: ")
                        emailsenha = f"{email}{senha}"
                    
                    elif cadastrar == 's':
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
                    
                    else:
                        clear_console()
                        print("\nFormato não aceito!")
                        
                        time.sleep(2)
                        clear_console()
                    
                    f.close()
                    f = open("cadastros.txt", "r")
                    t = f.read()
                    
                    if emailsenha in t:
                        break
            
            f.close()
            clear_console()
            print("Login realizado com sucesso!")
            time.sleep(2)
            clear_console()
            exit()

    else:
        print("Formato não aceito!")
        time.sleep(2)
        clear_console()
