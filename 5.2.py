import numpy as np

m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))

A = np.array([list(map(int, input().split())) for _ in range(m)])

col = -1

for j in range(n):
    if np.any(A[:, j] == 0):
        col = j

if col != -1:
    A[:, [0, col]] = A[:, [col, 0]]
else:
    print("Столбцов с нулевыми элементами нет")

print(A)

K = int(input("K = "))

rows_sum = np.sum(A, axis=1)

idx = np.where(rows_sum <= K)[0]

if len(idx) > 0:
    A = np.delete(A, idx[0], axis=0)

print(A)

col = -1

for j in range(n):
    if np.all(A[:, j] < 0):
        col = j

if col != -1:
    zeros = np.zeros((m, 1), dtype=A.dtype)
    A = np.insert(A, col + 1, zeros.T, axis=1)

print(A)
