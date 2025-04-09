def get_valid_float(promt):
    """Функція для введення дійсного числа,яке більше за 0"""
    while True:
        try:
            value = float(input(promt))
            if value > 0:
                return value
            else:
                print("Помилка: введене число має бути більше 0!")



def get_valid_int(promt):
    """Функція для введення цілого числа,яке більше за 0"""
    while True:
        try:
            value = int(input(promt))
            if value > 0:
                return value
            else:
                print("Помилка: введене число має бути більше 0!")
        except ValueError:
            print("Помилка: введіть ціле число!")

bill = get_valid_float("Введіть суму рахунку: ")
tip_percent = get_valid_int("Введіть відсоток чайових (тільки ціле число, наприклад, 10): ")
people = get_valid_int("Введіть кількість людей (або 1,якщо ви самі: ")

tip_amount = bill * (tip_percent / 100)
total_amount = bill + tip_amount
amount_per_person = total_amount / people

print("\nЧайові: {:.2f} грн".format(tip_amount))
print("Загальна сума до оплати: {:.2f} грн".format(total_amount))
print("Кожен має заплатити: {:.2f} грн".format(amount_per_person))