import random

num_c = random.randint(0, 10)
num_t = 4

#o prof infelizmente não deixa usar laço de reptição! então vai ser no caminho da dor msm
# com laço de repetição:
#
#for t in num_t:
#    tentativa = int(input("numero entre 0 a 10 > "))
#    if tentativa != num_c:
#        num_t - 1
#        print(f"Você errou! Num de tentativas restantes: {num_t}")
#    else:
#        print("Acertou")
#
# Sem laço de repetição:

tent = int(input("Num entre 0 a 10 > "))
if tent != num_c:
    num_t - 1
    print(f"tente mais uma vez. num de tentativas: {num_t}")
    tent2 = int(input("Num entre 0 a 10 > "))
    if tent2 != num_c:
        print(f"tente mais uma vez. num de tentativas: {num_t}")
        num_t - 1
        tent3 = int(input("Num entre 0 a 10 > "))
        if tent3 != num_c:
            print(f"tente mais uma vez. num de tentativas: {num_t}")
            num_t - 1
            tent4 = int(input("Num entre 0 a 10 > "))
            if tent4 != num_c:
                num_t - 1
                print("Tentativas esgotadas")
            else:
                print("Você acertou!")
        else:
            print("Você acertou!")
    else:
        print("Você acertou!")
else:
    print("Você acertou!")

#esse ai deu até dor de fazer pqp

    
