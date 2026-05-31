import numpy as np

n = int(input("Размер матрицы: "))

A = np.array([list(map(int, input().split())) for _ in range(n)])

i, j = np.indices((n, n))

B = A[i + j < n - 1]

print("Матрица:")
print(A)

print("Одномерный массив:")
print(B)

sums = np.sum(A, axis=0)

for j in range(n):
    if sums[j] % 3 == 0 or sums[j] % 7 == 0:
        A[:, j] = np.sort(A[:, j])

print("Результат:")
print(A)
