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

frequencies = letter_frequencies(CIPHERTEXT)

for letter, count in frequencies[:8]:
    print(f"{letter}: {count}")
total_letters = sum(count for letter, count in frequencies)
print(f"Total letters: {total_letters}")