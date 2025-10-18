n = int(input("Введи число n (1 ≤ n ≤ 100000): "))

print(f"Числа-паліндроми, які не перевищують {n}:")

for i in range(1, n + 1):
    if str(i) == str(i)[::-1]:
        print(i)