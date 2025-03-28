import random

c_val = float(input("Valor da moeda: R$"))
#qntd = int(input("Qntd de moedas: "))

v_base = 299 #random.randint(100, 299)
v_desc = (v_base*c_val) - (((c_val*300)*5)/100)

if v_base * c_val < v_desc:
    print(f"a quantidade de moedas {v_base} tem um valor menor que, 300 já que mesmo com desconto o valor é maior: sem desconto: {v_base*c_val}, com desconto: {v_desc}")
else:
    print(f"a quantidade de moedas maior que 300 tem um valor menor que, {v_base} já que com desconto o valor é menor: sem desconto: {v_base*c_val}, com desconto: {v_desc}")