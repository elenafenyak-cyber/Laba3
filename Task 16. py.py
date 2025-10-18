# Введення числа n
n = int(input("Введіть число n (≤9): "))

print(f"Драбинка з {n} сходинок:")

# Формування драбинки
for i in range(1, n + 1):
    # Формуємо рядок від 1 до i
    row = ""
    for j in range(1, i + 1):
        row += str(j)
    print(f"Сходинка {i}: {row}")