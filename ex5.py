USER1 = "ROSSINI"
USER2 = "Allana"
PASSWORD = "1357"

while True:
    usr_input = input("Username: ")

    if usr_input == USER1 or usr_input == USER2:
        print("Username finded")
        pass_input = input("senha: ")
        if pass_input == PASSWORD:
            print("login realizado")
            break
        else:
            print("password or username, not equals")
    else:
        print("username not founded")
