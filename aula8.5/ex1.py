import numpy as np
import termcolor

x = list(map(int, input(termcolor.colored("'x': [x,x,x](x3) > ",color='yellow')).split()))
y = list(map(int, input(termcolor.colored("'y': [x,x,x](x3) > ", color='yellow')).split()))

X = np.array(([x[0], x[1], x[2]], [x[3], x[4], x[5]], [x[6], x[7], x[8]]))
Y = np.array(([y[0], y[1], y[2]], [y[3], y[4], y[5]], [y[6], y[7], y[8]]))


det_x = np.linalg.det(X)
print(f'determinate de X: {det_x}')
det_y = np.linalg.det(Y)
print(f'determinate de Y: {det_y}')

if det_x != 0 and det_y != 0:
    print(termcolor.colored("matriz não linear", color='red'))
else:
    print(termcolor.colored("matriz linear", color='green'))