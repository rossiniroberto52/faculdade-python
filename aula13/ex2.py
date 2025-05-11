num_t = 1
num_m = 1

while num_t <= 10:
    while num_m <= 10:
        linha = num_m * num_t
        print(f"{num_m} x {num_t} = {linha}")
        num_m += 1
    print("\n")
    num_t += 1
    num_m = 1