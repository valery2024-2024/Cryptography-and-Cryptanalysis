# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №5
# Тема: Повний перебір і частотний аналіз

CIPHERTEXT = (
    "AOL ILZA DHF AV BUKLYZAHUK H DLHR JPWOLY PZ AV IYLHR PA VU ZHML "
    "AYHPUPUN KHAH. JHLZHY OHZ H ZTHSS RLF ZWHJL, ZV IYBAL MVYJL JHU "
    "AYF LCLYF ZOPMA. SLAALY MYLXBLUJPLZ JHU OLSW YHUR YLZBSAZ, IBA "
    "AOLF HYL VUSF H JSBL."
)

BEST_SHIFT = 7

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

def letter_frequencies(text: str) -> list[tuple[str, int]]:
    frequencies = {}

    for char in text:
        if "A" <= char <= "Z":
            frequencies[char] = frequencies.get(char, 0) + 1

    return sorted(
        frequencies.items(),
        key=lambda item: item[1],
        reverse=True
    )

def frequency_shift_candidates(
    frequencies: list[tuple[str, int]]
) -> list[tuple[str, str, int]]:
    common_plaintext_letters = ["E", "T", "A"]
    candidates = []

    for cipher_letter, _ in frequencies[:3]:
        for plain_letter in common_plaintext_letters:
            shift = (
                ord(cipher_letter) - ord(plain_letter)
            ) % 26

            candidates.append(
                (cipher_letter, plain_letter, shift)
            )

    return candidates

def run_self_checks() -> None:
    # Контрольні приклади
    assert caesar_decrypt("KHOOR", 3) == "HELLO"
    assert caesar_decrypt("ABC XYZ!", 1) == "ZAB WXY!"

    # Shift = 0
    assert caesar_decrypt("HELLO", 0) == "HELLO"

    # Shift = 26 повинен працювати як shift = 0
    assert caesar_decrypt("HELLO", 26) == "HELLO"

    # Пробіли та пунктуація не змінюються
    assert caesar_decrypt("KHOOR, ZRUOG!", 3) == "HELLO, WORLD!"

    # Порожній рядок
    assert caesar_decrypt("", 5) == ""

    # Brute force повинен повернути рівно 26 варіантів
    assert len(brute_force_caesar("KHOOR")) == 26

run_self_checks()
print("LAB5_OK")

print("\nTOP FREQUENCIES:")

frequencies = letter_frequencies(CIPHERTEXT)

for letter, count in frequencies[:8]:
    print(f"{letter}: {count}")
total_letters = sum(count for letter, count in frequencies)
print(f"Total letters: {total_letters}")

candidates = frequency_shift_candidates(frequencies)

print("\nSHIFT CANDIDATES:")

for cipher_letter, plain_letter, shift in candidates:
    print(
        f"{cipher_letter} -> {plain_letter}: "
        f"shift={shift:02d}"
    )

brute_force_results = brute_force_caesar(CIPHERTEXT)

print("\nBRUTE FORCE:")

for shift, decrypted_text in brute_force_results:
    print(f"shift={shift:02d}: {decrypted_text}")

plaintext = caesar_decrypt(CIPHERTEXT, BEST_SHIFT)

print("\nBEST SHIFT:")
print(BEST_SHIFT)

print("\nPLAINTEXT:")
print(plaintext)

# Висновок:
# Brute force для шифру Цезаря практичний, тому що існує лише 26 можливих зсувів.
# Найчастіші літери L, H та A дали корисну підказку, а shift 7 з'явився у кількох частотних гіпотезах.
# Частотний аналіз сам по собі не гарантує правильний результат, тому що частоти залежать від довжини та змісту тексту.
# Shift 7 обрано тому, що після розшифрування отримано зв'язний і зрозумілий англійський текст.

