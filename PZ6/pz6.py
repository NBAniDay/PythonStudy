import random

def generate_receipt(file_name="receipt.txt"):
    # Список товарів (назва, ціна в грн)
    products = [
        ("Хліб", 25.00),
        ("Молоко", 40.50),
        ("Цукор", 30.00),
        ("Чай", 85.00),
        ("Кава", 150.00),
        ("Масло", 80.00),
        ("Сир", 120.00),
        ("Яйця", 45.00),
        ("Йогурт", 35.00)
    ]

    # Випадковий вибір від 3 до 7 товарів
    selected_products = random.sample(products, random.randint(3, 7))

    # Запис у файл
    with open(file_name, "w", encoding="utf-8") as file:
        for name, price in selected_products:
            file.write(f"{name},{price}\n")

    print("Чек збережено у файл", file_name)

def analyze_receipt(file_name="receipt.txt"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            items = [line.strip().split(",") for line in file.readlines()]

        items = [(name, float(price)) for name, price in items]

        total = sum(price for _, price in items)
        most_expensive = max(items, key=lambda x: x[1])
        cheapest = min(items, key=lambda x: x[1])

        # Вивід результатів
        print("Чек магазину:")
        print("-" * 30)
        for name, price in items:
            print(f"{name:<10} {price:>6.2f} грн")
        print("-" * 30)
        print(f"Загальна сума: {total:.2f} грн")
        print(f"Найдорожчий товар: {most_expensive[0]} ({most_expensive[1]:.2f} грн)")
        print(f"Найдешевший товар: {cheapest[0]} ({cheapest[1]:.2f} грн)")

    except FileNotFoundError:
        print("Файл чека не знайдено! Спочатку згенеруйте чек.")

# Виконання
generate_receipt()
analyze_receipt()