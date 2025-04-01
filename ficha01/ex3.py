value = float(input("valor da conta: "))
qntd_p = int(input("qntd de pessoas: "))

if value >= 150 and qntd_p >= 4: #desconto de 10%
    res = value - ((value * 10)/100)
    print(f"o valor da compra com desconto de 10%: {res}")
else: #desconto de 5%
    res = value - ((value * 5)/100)
    print(f"o valor da compra com desconto de 5%: {res}")