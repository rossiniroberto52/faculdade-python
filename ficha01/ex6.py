import random, string

alafabeto = list(string.ascii_lowercase)
num_letra = random.randint(0,25)

t1 = input("Qual a letra sorteada: ")
if t1 == alafabeto[num_letra]:
    print("acertou!")
else:
    print("Errou! tente novamente!")
    t2 = input("qual a letra sorteada: ")
    if t2 == alafabeto[num_letra]:
        print("acertou")
    else:
        print("Errou!, fim do programa!")