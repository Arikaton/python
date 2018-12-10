import matplotlib.pyplot as plt
from math import atan

# система Y'' + Y' + Y = B*U
b = int(input('Введите В\n'))
w = [i/100 for i in range(1, 2000, 1)]
del(w[99])
A, B = [], []
for i in w:
    P = (-b*i**2+b)/(i**4-i**2+1)
    Q = (i*b)/(i**4-i**2+1)
    A.append((P**2 + Q**2)**(1/2))
    B.append(atan(Q/P))

plt.plot(w, A)
plt.plot(w, B)
plt.show()