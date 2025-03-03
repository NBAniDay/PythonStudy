import re

def check_password(password: str) -> bool:
    if len(password) < 8:
        print("Пароль має бути не коротшим за 8 символів")
        return False
    if not re.search(r"[A-Z]", password):
        print("Пароль має містити хоча б одну літеру у верхньому регістрі.")
        return False
    if not re.search(r"\d", password):
        print("Пароль має містити хоча б одну цифру.")
        return False
    return True

while True:
    password = input("Введіть пароль: ")
    if check_password(password):
        print("Пароль прийнято")
        break