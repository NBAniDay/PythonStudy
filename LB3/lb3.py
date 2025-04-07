def is_prime(n):
    """Перевірка чи просте число"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    """Основна функція програми."""
    n = int(input("Введіть число: "))

    if is_prime(n):
        print(f"{n} є простим числом. Прості числа до {n}:")
        for i in range(2, n + 1):
            if is_prime(i):
                print(i, end=" ")
    else:
        print(f"{n} є складеним числом. Складені числа до {n}:")
        for i in range(2, n + 1):
            if not is_prime(i):
                print(i, end=" ")

# Виклик основної функції
main()