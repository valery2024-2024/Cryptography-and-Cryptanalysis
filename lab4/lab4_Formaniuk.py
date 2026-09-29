# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №4
# Тема: Шифр Віженера та перестановки

def validate_vigenere_key(key: str) -> None:
    if not key:
        raise ValueError("Key must not be empty")

    if not all("A" <= char <= "Z" for char in key):
        raise ValueError("Key must contain only A-Z letters")
    