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

def validate_permutation_order(order: list[int]) -> None:
    if not order:
        raise ValueError("Order must not be empty")

    if sorted(order) != list(range(len(order))):
        raise ValueError("Order must be a valid permutation")

def permutation_encrypt(text: str, order: list[int]) -> str:
    validate_permutation_order(order)

    result = ""
    block_size = len(order)

    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]

        if len(block) < block_size:
            result += block
        else:
            for index in order:
                result += block[index]

    return result

def permutation_decrypt(text: str, order: list[int]) -> str:
    validate_permutation_order(order)

    result = ""
    block_size = len(order)

    inverse_order = [0] * block_size
    for i, index in enumerate(order):
        inverse_order[index] = i

    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]

        if len(block) < block_size:
            result += block
        else:
            for index in inverse_order:
                result += block[index]

    return result

def run_vigenere_tests() -> None:
    # 1. Контрольний приклад
    assert vigenere_encrypt("HELLOWORLD", "KEY") == "RIJVSUYVJN"

    # 2. Round-trip з пробілами та пунктуацією
    text = "ATTACK AT DAWN!"
    encrypted = vigenere_encrypt(text, "LEMON")

    assert encrypted == "LXFOPV EF RNHR!"
    assert vigenere_decrypt(encrypted, "LEMON") == text

    # 3. Рядок із цифрами та пунктуацією
    text_with_symbols = "TEST 123!"
    encrypted_with_symbols = vigenere_encrypt(text_with_symbols, "KEY")

    assert vigenere_decrypt(encrypted_with_symbols, "KEY") == text_with_symbols

    # 4. Порожній ключ повинен бути відхилений
    try:
        vigenere_encrypt("HELLO", "")
        assert False
    except ValueError:
        pass

    # 5. Некоректний ключ повинен бути відхилений
    try:
        vigenere_encrypt("HELLO", "K3Y")
        assert False
    except ValueError:
        pass

run_vigenere_tests()
