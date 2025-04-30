import re

def translated_text(ukrainian_text: str) -> str:
    dictionary = {
        "я": "I", "люблю": "love", "програмування": "programming",
        "привіт": "hello", "світ": "world", "це": "this is",
        "мій": "my", "котик": "cat", "гарний": "beautiful"
    }

    # Функція для перекладу 1 слова
    def translate_word(word: str) -> str:
        lower_word = word.lower()
        translated = dictionary.get(lower_word, word)  # Перекладаємо слово, якщо є у словнику
        return translated.capitalize() if word.istitle() else translated

    # Розбиваємо рядок на слова, пробіли та символи пунктуації
    words = re.findall(r"\b\w+\b|\s+|[^\w\s]", ukrainian_text)

    # Перекладаємо кожне слово
    translated_result = "".join(
        translate_word(word) if word.strip() else word for word in words
    )  # ❗ виправлено назву змінної

    return translated_result  # ❗ повертаємо результат

# Введення користувача
text = input("Введіть текст українською: ")
translated = translated_text(text)
print("Переклад:", translated)
