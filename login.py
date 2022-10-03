import os
import time

def clear_console():
    os.system('cls')
    
def delayed_clear_console(n):
    time.sleep(n)
    clear_console()
    


while True:
    cadastrado = input("Você já é cadastrado [s/n]?\n").lower()
    
    if cadastrado == 'n':
        while True:
            email = input("Digite o e-mail que deseja cadastrar: ")
            senha = input("Digite a senha que deseja cadastrar: ")
            senhav = input("Digite a senha novamente: ")
            
            while senha != senhav:
                senhav = input("A senha não corresponde! Digite novamente: ")
                
            clear_console()
            
            emailsenha = f"{email}{senha}\n"
            
            f = open("cadastros.txt", "a")
            f.close()
            f = open("cadastros.txt", "r")
            a = f.read()
            f.close()
            
            if emailsenha in a:
                cadastrar1 = input("Esse email já está cadastrado!\n\nDeseja realizar o login [s/n]").lower()
                if cadastrar1 == 's':
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
                                    
                                    delayed_clear_console(2)
                                    exit()
                                
                                else:
                                    clear_console()
                                    print("\nFormato não aceito!")
                                    
                                    delayed_clear_console(2)
                                
                                f.close()
                                f = open("cadastros.txt", "r")
                                t = f.read()
                                
                                if emailsenha in t:
                                    break
                        
                        f.close()
                        clear_console()
                        print("Login realizado com sucesso!")
                        delayed_clear_console(2)
                        exit()
                
                else:
                    while cadastrar1 not in 'sn':
                        print("Formato não aceito!")
                        
                        delayed_clear_console(2)
                        
                        cadastrar1 = input("Deseja realizar o login [s/n]").lower()
                        clear_console()
            
            else:  
                print("Cadastro realizado com sucesso!")
                
                f = open("cadastros.txt", "a")
                f.writelines(emailsenha)
                f.close()
                
                delayed_clear_console(2)
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
                        
                        delayed_clear_console(2)
                        exit()
                    
                    else:
                        clear_console()
                        print("\nFormato não aceito!")
                        
                        delayed_clear_console(2)
                    
                    f.close()
                    f = open("cadastros.txt", "r")
                    t = f.read()
                    
                    if emailsenha in t:
                        break
            
            f.close()
            clear_console()
            print("Login realizado com sucesso!")
            delayed_clear_console(2)
            exit()

    else:
        print("Formato não aceito!")
        delayed_clear_console(2)
