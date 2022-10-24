import math as m


def MultiplyMatrix(M1, M2):
    matrix = []
    for i in range(len(M1)):
        matrix.append([])
        for j in range(len(M2[0])):
            matrix[i].append(0)

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                matrix[i][j] += M1[i][k] * M2[k][j]
    return matrix


def IdentityOp(a):
    matrix = []
    for i in range(0, a):
        matrix.append([])
        for j in range(0, a):
            if (i == j):
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix


def MV(M, V):
    matriz = []
    for fila in M:
        res = 0
        for col in range(len(fila)):
            res += (fila[col]*V[col])
        matriz.append(res)
    return matriz


def Cross(A, B):
    R = [A[1]*B[2] - A[2]*B[1],
         A[2]*B[0] - A[0]*B[2],
         A[0]*B[1] - A[1]*B[0]]
    return R


def Substract(A, B):
    R = [A[i] - B[i] for i in range(min(len(A), len(B)))]
    return R

def Add(A, B):
    R = [A[i] + B[i] for i in range(min(len(A), len(B)))]
    return R

def Normalize(V):
    L = m.sqrt(V[0]**2 + V[1]**2 + V[2]**2)
    VN = [
        V[0]/L, V[1]/L, V[2]/L
    ]
    return VN


def Dot(A, B):
    R = 0
    for i in range(len(A)):
        R += A[i]*-B[i]
    return R


def HEX(color):
    cr = color/255
    return cr


def transpuesta(m):
    return list(map(list, zip(*m)))


def Min(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def determinante(m):
    # Use in 2 x 2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*determinante(Min(m, 0, c))
    return determinant


def inv(m):
    cofactors = []
    determinant = determinante(m)

    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = Min(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * determinante(minor))
        cofactors.append(cofactorRow)
    cofactors = transpuesta(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
