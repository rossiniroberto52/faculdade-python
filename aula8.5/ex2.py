num1, num2, num3 = map(int, input().split())

if num1 == num2 == num3:
    print("Iguals")
elif num1 <= num2 <= num3:
    print("Ordem crescente")
elif num1 >= num2 >= num3:
    print("Ordem decrescente")
else:
    print("Sem ordem entre eles")