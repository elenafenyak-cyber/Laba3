print("Введи послідовність натуральних чисел (0 — щоб завершити):")

max_value = -1
max_index = -1
index = 0

while True:
    n = int(input(f"{index}-е число: "))
    if n == 0:
        break
    if n > max_value:
        max_value = n
        max_index = index
    index += 1

print(f"Найбільше число: {max_value}")
print(f"Його індекс: {max_index}")