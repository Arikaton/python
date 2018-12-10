print('Введите a и b через пробел')
a, b = [int(i) for i in input().split()]
t = 1
A = 4*b/(81+a**2)**0.5
print("Амплитуда равна: ", A)