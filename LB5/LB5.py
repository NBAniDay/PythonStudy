def analyze_reviews():
    # Списки ключових слів
    positive_words = {"чудово","супер","відмінно","гарно","клас","рекомендую","задоволений"}
    negative_words = {"погано","жахливо","не рекомендую","розчарований","марно","поганий"}

    # Отримання відгуків від користувача
    num_reviews = int(input("Введіть кількість відгуків: "))
    reviews = [input(f"Введіть відгук {i+1}: ").strip() for i in range(num_reviews)]

    # Аналіз відгуків
    positive_count = 0
    negative_count = 0
    total_length = 0

    for review in reviews:
        total_length += len(review)
        words = set(review.lower().split()) # Розбиваємо текст на слова та переводимо в нижній регістр
        if words & positive_words:
            positive_count += 1
        if words & negative_words:
            negative_count += 1

    # Визначення середньої довжини відгуку
    avg_length = total_length / num_reviews if num_reviews > 0 else 0

    # Знаходження найдовших відгуків (топ-3)
    longest_reviews = sorted(reviews, key=len, reverse=True)[:3]

    # Виведення результатів
    print("\nРезультати аналізу")
    print(f"Позитивн відгуки: {positive_count}")
    print(f"Негативні відгуки: {negative_count}")
    print(f"Середня довжина відгуку: {avg_length:.2f} символів")
    print("Найдовші відгуки")
    for i, review in enumerate(longest_reviews, 1):
        print(f" {i}. {review}")

if __name__ == "__main__":
    analyze_reviews()
