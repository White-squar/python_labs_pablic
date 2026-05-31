import numpy as np

n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))

A = np.array([list(map(int, input().split())) for _ in range(n)])

rows = np.arange(n).reshape(-1, 1)

mask = (A < 0) & (A % 2 != 0) & (np.abs(A) < rows)

elems = A[mask]

print("Матрица:")
print(A)

print("Сумма:", np.sum(elems))
print("Произведение:", np.prod(elems))


n = int(input("Размер матрицы: "))

A = np.array([list(map(int, input().split())) for _ in range(n)])

rows = np.where(np.all(A >= 0, axis=1))[0]

print("Матрица:")
print(A)

print("Номера строк:", rows)


n = int(input("Размер матрицы: "))

A = np.array([list(map(int, input().split())) for _ in range(n)])

i, j = np.indices((n, n))

mask = (i + j > n - 1) & (A > 0)

print("Матрица:")
print(A)

if np.any(mask):
    print("Минимальный положительный элемент:", np.min(A[mask]))
else:
    print("Под побочной диагональю нет положительных элементов")
