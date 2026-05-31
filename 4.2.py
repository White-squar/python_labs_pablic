a = [int(input()) for _ in range(int(input("введите колчиесвто элементов: ")))]


last_neg = -1

for i in range(len(a)):
    if a[i] < 0:
        last_neg = i

if last_neg == -1:
    print("Отрицательных элементов нет")
else:
    print("Номер последнего отрицательного:", last_neg)
    print("Элементы слева от него:", a[:last_neg])
    
n1 = int(input("введиите левый индекс: "))
n2 = int(input("введите правый индекс: "))

i = n1

while i <= n2 and i < len(a):
    if a[i] % 2 != 0:
        del a[i]
        n2 -= 1
    else:
        i += 1

print(a)

x = int(input("введите число для вставки: "))

i = 0

while i < len(a):
    if a[i] % 2 == 0 and a[i] % 10 != 0:
        a.insert(i + 1, x)
        i += 2
    else:
        i += 1

print(a)
