a, b, c = map(int, input().split())

if a == b and a != c:
    print("dois são iguais e o terceiro é diferente")
elif a == c and a != b:
    print("dois são iguais e o terceiro é diferente")
elif b == c and b != a:
    print("dois são iguais e o terceiro é diferente")
elif a == b == c:
    print("são todos iguais")