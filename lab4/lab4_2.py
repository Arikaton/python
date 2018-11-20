from random import randint
import math
import matplotlib.pyplot as plt
import sympy as sp
import re


# класс массивов, похожий на array в NumPy
class array:
    def __init__(self, a):
        self.a = a
        try:
            c = len(self.a[0])
            self.shape = (len(self.a), c)
        except:
            self.shape = (1, len(self.a))

    # транспонирование
    def T(self):
        if self.shape[0] == 1:
            res = [[self.a[i]] for i in range(self.shape[1])]
        elif self.shape[1] == 1:
            res = []
            for i in range(self.shape[0]):
                res.append(self.a[i][0])
        else:
            res = list(zip(*self.a))
            for i in range(len(res)):
                res[i] = list(res[i])
        self.shape = (self.shape[1], self.shape[0])
        return array(res)

    # умножение
    def dot(self, any):
        if any.shape[1] == 1 and self.shape[0] != 1:
            res = [[0] for i in range(any.shape[0])]
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    res[i][0] += self.a[i][j] * any.a[j][0]
        elif self.shape[0] == 1:
            res = [0 for i in range(any.shape[1])]
            for i in range(any.shape[1]):
                for j in range(self.shape[1]):
                    res[i] += self.a[j] * any.a[j][i]
        else:
            res = [[0 for i in range(any.shape[1])] for j in range(self.shape[1])]
            for i in range(self.shape[0]):
                for j in range(any.shape[1]):
                    for k in range(self.shape[1]):
                        res[i][j] += self.a[i][k] * any.a[k][j]
        self.shape = (self.shape[0], any.shape[1])
        return array(res)

    # срез
    def slice(self, i, j):
        res = [[0 for i in range(self.shape[0] - 1)] for j in range(self.shape[1] - 1)]
        for _ in range(self.shape[0]):
            for k in range(self.shape[1]):
                if _ < i and k < j:
                    res[_][k] = self.a[_][k]
                elif _ > i and k < j:
                    res[_ - 1][k] = self.a[_][k]
                elif _ < i and k > j:
                    res[_][k - 1] = self.a[_][k]
                elif _ > i and k > j:
                    res[_ - 1][k - 1] = self.a[_][k]
        return array(res)

    # определитель
    def det(self):
        if self.shape[0] == self.shape[1]:
            if self.shape[0] == 1:
                return self.a[0][0]
            elif self.shape[0] == 2:
                return self.a[0][0] * self.a[1][1] - self.a[0][1] * self.a[1][0]
            else:
                res = 0
                for i in range(self.shape[0]):
                    res += self.a[0][i] * (-1) ** (i) * self.slice(0, i).det()
            return res
        else:
            print("Матрица не квадратная")

    # алгебраическое дополнение
    def alg(self, i, j):
        return (-1) ** (i + j) * self.slice(i, j).det()

    # обратная матрица
    def inv(self):
        return array([[self.alg(i, j) for i in range(self.shape[0])] for j in range(self.shape[1])]) * (1 / self.det())

    # перегрузка операторов \/
    def __str__(self):
        return str(self.a)

    def __getitem__(self, item):
        return self.a[item]

    def __setitem__(self, key, value):
        self.a[key] = value

    def __mul__(self, other):
        return array([[self.a[i][j] * other for i in range(self.shape[0])] for j in range(self.shape[1])])

    def __sub__(self, any):
        return array([[self.a[i][j] - any.a[i][j] for i in range(self.shape[0])] for j in range(self.shape[1])])


# еденичная матрица
def ones(size=2, value=1):
    c = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                c[i][j] = value
    return array(c)


# функция рисует график уравнения
def paint(a, b, c, l, r):
    f = []
    for i in range(l, r):
        if i == 0:
            pass
        else:
            f.append(c.dot((ones(3, i) - a).inv()).dot(b)[0])
    x = list(range(l, r))
    x.remove(0)
    plt.plot(x, f)
    plt.show()


# решение квадратного уравнения
def solve_square(a):
    a = re.findall(r'\(.*\)', a)[0]
    a = re.sub(r'\s+', '', a)
    A, _, B, C = re.findall(r'[-+]?[ ]?\d+', a)
    A, B, C = int(A), int(B), int(C)
    D = int(B) ** 2 - 4 * int(A) * int(C)
    x1, x2 = (-B + D ** 0.5) / (2 * A), (-B - D ** 0.5) / (2 * A)
    return x2, x1


# определяет знак числа
def sgn(x):
    return 1 if x >= 0 else -1


# решает кубическое уравнение методом виетта
def solve_cube(b):
    b = re.findall(r'\(.*\)', b)[0]
    b = re.sub(r'\s+', '', b)
    _, A, __, B, C = re.findall(r'[-+]?[ ]?\d+', b)
    A, B, C = int(A), int(B), int(C)
    Q = (A ** 2 - 3 * B) / 9
    R = (2 * A ** 3 - 9 * A * B + 27 * C) / 54
    S = Q ** 3 - R ** 2
    if S > 0:
        ph = (math.acos(R / (Q ** (3 / 2)))) / 3
        x1 = -2 * (Q ** 0.5) * math.cos(ph) - A / 3
        x2 = -2 * (Q ** 0.5) * math.cos(ph + 2 * math.pi / 3) - A / 3
        x3 = -2 * (Q ** 0.5) * math.cos(ph - 2 * math.pi / 3) - A / 3
    elif S < 0:
        ph = math.acosh(abs(R) / (Q ** (3 / 2))) / 3
        x1 = -2 * sgn(R) * abs(Q) ** 0.5 * math.cosh(ph) - A / 3
        x2 = complex(sgn(R) * abs(Q) ** 0.5 * math.cosh(ph) - A / 3, (3 * abs(Q)) ** 0.5 * math.sinh(ph))
        x3 = complex(sgn(R) * abs(Q) ** 0.5 * math.cosh(ph) - A / 3, -(3 * abs(Q)) ** 0.5 * math.sinh(ph))
    else:
        x1 = -2 * math.pow(R, 1 / 3) - A / 3
        x2 = x3 = math.pow(R, 1 / 3) - A / 3
    return x1, x2, x3


# массивы со случайными значениями
A = array([[randint(0, 10) for i in range(3)] for j in range(3)])  # 3x3
B = array([[randint(0, 10)] for i in range(3)])  # 3x1
C = array([randint(0, 10) for i in range(3)])  # 1x3

if __name__ == '__main__':
    x = sp.symbols('s')  # инициализация символьной переменной
    res = sp.factor(C.dot((ones(3, x) - A).inv()).dot(B)[0])  # решение уравнения
    pattern = r'.*\(.*\)\/'
    a = re.findall(pattern, str(res))
    a = a[0][:-1]       # числитель уравнения
    print(a)
    b = str(res)
    b = b[len(a) + 1:]  # знаменатель уравнения
    print("Уравнение:", res)
    dec = solve_square(a), solve_cube(b)
    print(
        'Корни числителя: {0}; {1}\nКорни знаменателя: {2}; {3}; {4}'.format(dec[0][0], dec[0][1], dec[1][0], dec[1][1],
                                                                             dec[1][2]), '\n')

    flag = True
    for i in range(len(dec[0])):
        for j in range(len(dec[1])):
            if dec[0][i] == dec[1][j]:
                print('проблемы с управляемостью/наблюдаемостью')
                flag = False
                break
    if flag:
        print('нет проблемы с управляемостью/наблюдаемостью')

    # проверка на устойчивость
    zero = False
    flag = True
    for i in range(3):
        if dec[1][i].real > 0:
            print('система неустойчива')
            flag = False
            break
        elif dec[1][i].real == 0:
            zero += True
    if flag:
        if zero:
            print('система находится на границе устойчивости')
        else:
            print('система устойчива')