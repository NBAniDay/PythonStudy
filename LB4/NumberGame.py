def can_reach_number(n):
    if n == 1:
        return True
    if n < 1:
        return False

    if n % 2 == 0:
        return can_reach_number(n // 2)
    else:
        return can_reach_number(n - 7)

# Ввід числа
n = int(input("Введіть число: "))

# Перевірка
if can_reach_number(n):
    print("Так можна отримати 1")
else:
    print("Ні, не можна отримати 1")