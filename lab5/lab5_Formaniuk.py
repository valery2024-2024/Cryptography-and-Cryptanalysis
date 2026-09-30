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

