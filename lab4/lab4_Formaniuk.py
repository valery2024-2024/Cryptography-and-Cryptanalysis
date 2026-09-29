# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №4
# Тема: Шифр Віженера та перестановки

def validate_vigenere_key(key: str) -> None:
    if not key:
        raise ValueError("Key must not be empty")

    if not all("A" <= char <= "Z" for char in key):
        raise ValueError("Key must contain only A-Z letters")

def vigenere_encrypt(text: str, key: str) -> str:
    validate_vigenere_key(key)

    result = ""
    key_index = 0

    for char in text:
        if "A" <= char <= "Z":
            x = ord(char) - ord("A")
            shift = ord(key[key_index % len(key)]) - ord("A")
            y = (x + shift) % 26

            result += chr(y + ord("A"))
            key_index += 1
        else:
            result += char

    return result
def vigenere_decrypt(text: str, key: str) -> str:
    validate_vigenere_key(key)

    result = ""
    key_index = 0

    for char in text:
        if "A" <= char <= "Z":
            y = ord(char) - ord("A")
            shift = ord(key[key_index % len(key)]) - ord("A")
            x = (y - shift) % 26

            result += chr(x + ord("A"))
            key_index += 1
        else:
            result += char

    return result


