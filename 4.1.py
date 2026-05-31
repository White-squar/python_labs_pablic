a = [int(input()) for _ in range(int(input("введите колчиесвто элементов: ")))]

# 1. Количество элементов, равных минимальному
mn = min(a)
count_min = sum(map(lambda x: x == mn, a))

# 2. Номер первого из двух последовательных элементов, произведение которых минимально
products = map(lambda i: a[i] * a[i + 1], range(len(a) - 1))
min_prod = min(products)

first_index = next(
    filter(
        lambda i: a[i] * a[i + 1] == min_prod,
        range(len(a) - 1)
    )
)

# 3. Количество и сумма отрицательных элементов,  не превышающих среднее арифметическое
avg = sum(a) / len(a)

count_neg = 0
sum_neg = 0

for x in filter(lambda x: x < 0 and x <= avg, a):
    count_neg += 1
    sum_neg += x
