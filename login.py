import os

#Clear console
def clear_console():
    os.system("cls")

clear_console()

login = input("Register your login: ")
password = input("Register your password: ")

login_password = {login: password}

clear_console()

i = False
tries = 0

while not i:
    if tries < 3:
        inserted_login = input("Type your login: ")
        inserted_password = input("Type your password: ")

        if login == inserted_login:
            if login_password[login] == inserted_password:
                print("Access guaranteed!")
        else:
            clear_console()
            print("Access denied!")
        i = (login == inserted_login) and (password == inserted_password)
    else:
        clear_console()
        print("Too many access tries!\nShutting down system...")
        exit()
    tries+=1

clear_console()

access_code = 0

while access_code == 0:
    access_code = input("Register your access code: ")

clear_console()

inserted_access_code = input("Type your access code: ")

tries = 0

while inserted_access_code != access_code:
    if tries < 2:
        clear_console()
        inserted_access_code = input("Access denied!\nType your access code: ")
    else:
        clear_console()
        print("Too many access tries!\nShutting down system...")
        exit()
    
    tries+=1
    

clear_console()

print("Full system access guaranteed!")
