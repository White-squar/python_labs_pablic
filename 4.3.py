a = [int(input()) for _ in range(int(input("введите колчиесвто элементов: ")))]

last_neg = -1

for i in range(len(a)):
    if a[i] < 0:
        last_neg = i

if last_neg > 1:
    a[1:last_neg] = sorted(a[1:last_neg], reverse=True)

print(a)

B = []
s = 0

for i in range(len(a)):
    s += a[i]
    B.append(s / (i + 1))

print(B)
