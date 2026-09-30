# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №5
# Тема: Повний перебір і частотний аналіз

def caesar_decrypt(text: str, shift: int) -> str:
    shift = shift % 26
    result = ""

    for char in text:
        if "A" <= char <= "Z":
            y = ord(char) - ord("A")
            x = (y - shift) % 26
            result += chr(x + ord("A"))
        else:
            result += char

    return result

def brute_force_caesar(text: str) -> list[tuple[int, str]]:
    results = []

    for shift in range(26):
        decrypted_text = caesar_decrypt(text, shift)
        results.append((shift, decrypted_text))

    return results

