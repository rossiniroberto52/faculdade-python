while True:
    num1, num2, num3 = map(int, input("o valor da soma dos numeros deve ser 3: ").split())
    if num1 + num2 + num3 == 10:
        print("operação realizada com sucesso")
        break
    else:
        print("Limite exedidio")
