import random
import string
from collections import Counter

def is_palindrome(word: str) -> bool:
    return word == word[::-1]

def is_evenly_balanced(word: str) -> bool:
    """
    Перевіряє, чи слово збалансоване:
    - Парна кількість усіх літер, або
    - Слово – паліндром
    """
    word = word.replace(" ", "").lower()  # ігноруємо пробіли та регістр

    if is_palindrome(word):
        return True

    letter_counts = Counter(word)
    for count in letter_counts.values():
        if count % 2 != 0:
            return False
    return True

def find_balanced_words(words: list[str]) -> list[str]:
    return [word for word in words if is_evenly_balanced(word)]

def find_longest_balanced_word(words: list[str]) -> str:
    balanced = find_balanced_words(words)
    if not balanced:
        return ""
    return max(balanced, key=lambda w: len(w.replace(" ", "")))  # довжина без пробілів

def generate_random_word(min_len=3, max_len=10) -> str:
    length = random.randint(min_len, max_len)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_words(n: int) -> list[str]:
    return [generate_random_word() for _ in range(n)]

# 🪐 Інтерактивний інтерфейс
def main():
    print("🌟 Ласкаво просимо на Парну планету!")
    print("1. Ввести власні слова")
    print("2. Згенерувати випадкові слова")
    print("3. Ввести фрази (з пробілами)")
    print("0. Вихід")

    while True:
        choice = input("\n🔢 Оберіть режим: ")

        if choice == "1":
            words_input = input("Введіть слова через кому: ")
            words = [w.strip() for w in words_input.split(",")]
        elif choice == "2":
            n = int(input("Скільки слів згенерувати? "))
            words = generate_random_words(n)
            print(f"📦 Згенеровані слова: {', '.join(words)}")
        elif choice == "3":
            phrases_input = input("Введіть фрази через кому: ")
            words = [w.strip() for w in phrases_input.split(",")]
        elif choice == "0":
            print("👋 До зустрічі на Парній планеті!")
            break
        else:
            print("❌ Невірний вибір. Спробуйте ще раз.")
            continue

        balanced = find_balanced_words(words)
        longest = find_longest_balanced_word(words)

        print("\n✅ Збалансовані слова/фрази:")
        if balanced:
            for w in balanced:
                print("  🔹", w)
            print(f"\n🏆 Найдовше збалансоване: {longest}")
        else:
            print("  😢 Нічого не знайдено")

if __name__ == "__main__":
    main()