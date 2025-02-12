import keyword
import string

def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False


    if name.count('_') == len(name) and len(name) > 1:
        return False

    if any(char.isupper() for char in name):
        return False

    allowed_chars = set(string.ascii_lowercase + string.digits + '_')
    if any(char not in allowed_chars for char in name):
        return False

    if name[0].isdigit():
        return False

    if not name:
        return False

    return True

user_input = input("Введіть ім'я змінної: ").strip()

print(is_valid_variable_name(user_input))

