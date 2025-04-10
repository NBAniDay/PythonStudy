# Відгуки, у списку
reviews = [
    "Ціна дуже висока для такого товару.",
    "Чудова якість, рекомендую!",
    "Мені сподобалась ціна та швидка доставка.",
    "Обслуговування жахливе.",
    "Не вартує своєї ціни."
]

# Додавання нових відгуків вручну
print("Введіть додаткові відгуки (щоб завершити — натисніть Enter):")
while True:
    review = input("Новий відгук: ")
    if review == "":
        break
    reviews.append(review)

# Фільтрація відгуків, що містять слово "ціна"
filtered_reviews = [review for review in reviews if "ціна" in review.lower()]

# Виведення результату
print("\nВідгуки, що містять слово 'ціна':")
for review in filtered_reviews:
    print("-", review)