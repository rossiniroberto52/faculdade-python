import math

def calcular_raizes(a,b,c):
    if a == 0:
        print("Impossivel calcular")
        return

    delta = -b**2 - 4 * a * c

    if delta < 0:
        print ("impossivel calcular")
        return

raiz_delta = math.sqrt(delta)
r1 = (-b + raiz_delta) / (2 * a)
r2 = (-b - raiz_delta) / (2 * a)
    
print(f"R1 = {r1:.5f}")
print(f"R2= {r2:.5f}")

a, b, c = map(float, input().split())
calcular_raizes(a, b, c)