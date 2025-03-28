while True:
    nome = input("Nome: ")
    if len(nome) <= 20:
        print("Operação realizada com sucesso!")
        break
    else:
        print(f'o nome {nome} tem mais de 20 caracteres!')
