from random import randint
import matplotlib.pyplot as plt


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def mean(ar):
    return sum(ar) / len(ar)


def ssum(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return sum(c)


# простое скользящее среднее
# s - размер окна для вычисления среднего
def sma_filter(y, s=10):
    r = [mean(y[i - s:i]) for i in range(s, len(y))]
    return r


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# взвешенное скользящее среднее
# s - размер окна для вычисления среднего
def wma_filter(y, s=10):
    w = [i for i in range(s, 0, -1)]  # веса элементов последовательности, самый "старый" имеет наибольший вес
    sw = sum(w)
    d = 2.0 / (s * (s + 1))
    r = [ssum(y[i - s:i], w) * d for i in range(s, len(y))]
    return r


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# экспоненциальное скользящее среднее
def ema_filter(y, p=50):
    r = [y[0]]
    for i in range(1, len(y)):
        r.append(r[-1] + 2.0 / (p + 1) * (y[i] - r[-1]))
    return r


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# экспоненциально взвешенное скользящее среднее  (фильтр Брауна)
def ewma_filter(y, p=0.15):
    r = [y[0]]
    for i in range(1, len(y)):
        r.append(p * y[i] + (1 - p) * r[-1])
    return r


WIDTH = 3

if __name__ == '__main__':
    l = [randint(0, 40) for i in range(40)]
    lx = [i for i in range(40)]
    s = sma_filter(l, WIDTH)
    sx = [i for i in range(WIDTH, len(s) + WIDTH)]
    w = wma_filter(l, WIDTH)
    e = ema_filter(l, 5)
    ew = ewma_filter(l)

    fig, ax = plt.subplots()

    ax.set_title('сглаживание')

    ax.plot(lx, l, label='исходные данные')
    ax.plot(sx, s, label='скользящее среднее')
    ax.plot(sx, w, label='взвешенное скользящее среднее')
    ax.plot(lx, e, label='экспоненциальное скользящее среднее')
    ax.plot(lx, ew, label='экспоненциальное взвешенное')
    ax.set_ylim(bottom=0, top=60)
    ax.legend(loc='upper left')
    plt.savefig('lab4_1')

    # fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    # ax1.plot(lx, l)
    # ax1.plot(sx, s)
    # ax1.plot(sx, w)
    # ax2.plot(lx, l)
    # ax2.plot(lx, e)
    # ax2.plot(lx, ew)
    plt.show()