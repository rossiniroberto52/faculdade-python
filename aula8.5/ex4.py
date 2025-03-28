import numpy as np

x1, x2 = map(int, input("x1 & x2: ").split())
y1, y2 = map(int, input("y1 & y2: ").split())


z = np.array([[x1, x2], [y1, y2]])  
print(f'Matriz:\n{z}')

det_z = np.linalg.det(z)
print(f'Determinante: {det_z}')

if det_z != 0:
    inv_z = np.linalg.inv(z)
    print(f'Matriz inversa:\n{inv_z}')
    identidade_verificada = np.allclose(z @ inv_z, np.eye(2))
    print(f'é identidade? {identidade_verificada}')
else:
    print("Matriz não invertível (determinante zero)")