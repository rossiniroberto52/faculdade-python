import math
a, b, c = map(float, input("a, b, c: ").split())
if a == 0:
    print("ERROR: 'a' não pode ser 0")
else:
    delta = b**2 - 4 * a * c
    if delta > 0:
        delta_root = math.sqrt(delta)
        x1 = (-b + delta_root) / (2*a)
        x2 = (-b - delta_root) / (2*a)
        print(f"Duas raízes reais distintas: {x1:.2f} e {x2:.2f}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Uma raiz real dupla: {x:.2f}")
    else:
        delta_root = math.sqrt(abs(delta))
        real_p = -b / (2*a)
        imagine_p = delta_root / (2*a)
        print(f"""
        Duas raíses complexas conjugadas:
        {real_p:.2f} + {imagine_p:.2f}
        {real_p:.2f} - {imagine_p:.2f}
        """)