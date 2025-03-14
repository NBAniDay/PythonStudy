correct_password = "1234"
attempts = 3

while attempts > 0:
    user_input = input("Введіть пароль: ")
    if user_input == correct_password:
        print("Доступ дозволено!")
        break
    else:
        attempts -= 1
        print(f"Неправильний пароль! Залишилось спроб: {attempts}")

if attempts == 0:
    print("Доступ заблоковано!")