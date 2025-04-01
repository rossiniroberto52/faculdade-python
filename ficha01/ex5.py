veicle_type = input("Tipo do veículo: ")
perm_time = int(input("tempo de permanencia(hrs): "))

if veicle_type == "carro" or veicle_type == "Carro":
    res = perm_time*5
    print(f"O valor a ser pago é de: R${res}")
elif veicle_type == "moto" or veicle_type == "Moto":
    res = perm_time*3
    print(f"O valor a ser pago é de: R${res}")
elif veicle_type == "outros" or veicle_type == "Outros":
    res = perm_time * 7
    print(f"O valor a ser pago é de: R${res}")
