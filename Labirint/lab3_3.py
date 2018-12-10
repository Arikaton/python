def size_m(matrix):
    m = len(matrix)
    return m


def mult(A1, A2):  # Умножение матриц
    n = len(A1)
    m = len(A2[0])
    res = []
    if (len(A1[0]) == len(A2)):
        for i in range(n):
            res.append([0] * m)
        for i in range(n):
            for j in range(m):
                for k in range(len(A2)):
                    res[i][j] += A1[i][k] * A2[k][j]
            return res
        else:
            print("mult is impossible")
        return res


def transp(A):
    n = len(A)
    m = len(A[0])
    trp = []
    for i in range(m):
        trp.append([0] * n)
    for i in range(m):
        for j in range(n):
            trp[i][j] = A[j][i]
    return trp


def constr(m, p):
    res1 = m
    for l in range(p - 1):
        res1 = mult(res1, m)
    return res1


def obs(m1, m2):
    A = []
    A += m1
    C = []
    C += m2
    r = []
    r += C
    n1 = len(m1)
    for g in range(n1 - 1):
        r += (mult(C, constr(A, g + 1)))
    r_obs = MatrixRank(r)
    if size_m(m1) == r_obs:
        print("Система наблюдаема, ранг матрицы наблюдаемости равен", r_obs)
    else:
        print("Система не наблюдаема, ранг равен матрицы наблюдаемости равен ", r_obs)


def contr(m1, m2):
    a1 = []
    b1 = []
    a1 += m1
    b1 += m2
    result = []
    N = len(m1)
    result += transp(b1)
    for t in range(N - 1):
        result += transp(mult(constr(a1, t + 1), b1))
    result = transp(result)
    r_contr = MatrixRank(result)
    if size_m(m1) == r_contr:
        print("Система управляема, ранг матрицы управляемости ", r_contr)
    else:
        print("Система не управляема, ранг матрицы управляемости ", r_contr)


m = [[2, 4, 1, 1],
     [0, 2, 1, 0],
     [2, 1, 1, 3],
     [4, 0, 2, 3]]

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[3], [2], [1]]
c = [[3, 5, 7]]


def swapRows(a, row1, row2):
    a[row2], a[row1] = a[row1], a[row2]
    return a


def Row_Transformation(a, x, row1, row2):
    for i in range(len(a[row2])):
        a[row2][i] += a[row1][i] * x
    return a


def MatrixRank(a):
    ncol = len(a[0])
    nrow = len(a)
    rank = min(ncol, nrow)

    if nrow > ncol:
        b = []
        for m in range(ncol):
            l = []
            for n in range(nrow):
                l.append(a[n][m])
            b.append(l)
        a = b
        ncol, nrow = nrow, ncol

    for r in range(rank):
        if a[r][r] != 0:
            for j in range(r + 1, nrow):
                a = Row_Transformation(a, -(a[j][r] // a[r][r]), r, j)
        else:
            count1 = True
            for k in range(r + 1, nrow):
                if a[k][r] != 0:
                    a = swapRows(a, r, k)
                    count1 = False
                    break

            if count1:
                for i in range(nrow):
                    a[i][r], a[i][rank - 1] = a[i][rank - 1], a[i][r]
            nrow -= 1

        count2 = 0
        for i in a:
            if i == [0] * ncol:
                count2 += 1

        return (rank - count2)


print(MatrixRank(m))
print(obs(a, c))
print(contr(a, b))
