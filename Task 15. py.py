# Зчитування числа n
n = int(input("Введіть число n: "))

# Початкова сума факторіалів
sum_factorials = 0

# Змінна для обчислення факторіалу
factorial = 1

# Цикл від 1 до n
for i in range(1, n + 1):
    factorial *= i  # обчислюємо i! поступово
    sum_factorials += factorial  # додаємо до суми

# Вивід результату
print(sum_factorials)