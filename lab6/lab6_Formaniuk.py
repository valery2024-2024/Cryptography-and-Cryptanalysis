# ПІБ: Форманюк Валерій
# Група: КН-4/1
# Лабораторна робота №6
# Тема: Повторне використання XOR-ключа

p1 = b"ATTACK AT DAWN!!"
p2 = b"RETREAT AT NOON!"
k1 = b"THIS_IS_TOY_KEY!"
k2 = b"ANOTHER_TOY_KEY!"

def xor_bytes(a: bytes, b: bytes) -> bytes:
    if len(a) != len(b):
        raise ValueError("lengths must match")
    return bytes(x ^ y for x, y in zip(a, b))

assert xor_bytes(b"\x00\xff", b"\xff\x00") == b"\xff\xff"
assert xor_bytes(b"AB", b"\x00\x00") == b"AB"

c1 = xor_bytes(p1, k1)
c2 = xor_bytes(p2, k1)

assert xor_bytes(c1, k1) == p1
assert xor_bytes(c2, k1) == p2

print("C1 HEX:", c1.hex())
print("C2 HEX:", c2.hex())

cipher_xor = xor_bytes(c1, c2)
plain_xor = xor_bytes(p1, p2)

assert cipher_xor == plain_xor

print("C1 XOR C2:", cipher_xor.hex())
print("P1 XOR P2:", plain_xor.hex())

# Ключ k1 зникає, тому що він використаний в обох шифротекстах.
# При XOR двох шифротекстів отримуємо k1 XOR k1 = 0, тому залишається тільки p1 XOR p2.

recovered_p2 = xor_bytes(cipher_xor, p1)
assert recovered_p2 == p2

print("RECOVERED P2:", recovered_p2.decode())

c2_fresh = xor_bytes(p2, k2)
fresh_cipher_xor = xor_bytes(c1, c2_fresh)

assert fresh_cipher_xor != plain_xor

# Коли для другого повідомлення використовується інший ключ k2,
# ключі k1 і k2 вже не знищують один одного при XOR.
# Тому C1 XOR C2 більше не дорівнює P1 XOR P2,
# і попередній простий спосіб відновлення p2 не працює.

print(
    "FRESH-KEY COMPARISON:",
    "different" if fresh_cipher_xor != plain_xor else "same"
)

assert len(p1) == len(p2) == len(k1) == len(k2)
assert xor_bytes(xor_bytes(p1, k1), k1) == p1
assert xor_bytes(xor_bytes(p2, k1), k1) == p2
assert xor_bytes(c1, c2) == xor_bytes(p1, p2)
assert recovered_p2 == p2
assert xor_bytes(c1, c2_fresh) != xor_bytes(p1, p2)

print("LAB6_OK")

# Висновок:
# Повторне використання ключа k1 для p1 і p2 небезпечне, тому що однаковий ключ зникає при XOR двох шифротекстів.
# Значення c1 XOR c2 розкриває p1 XOR p2, тобто залежність між двома відкритими повідомленнями.
# Якщо p1 відомий, то за допомогою c1 XOR c2 і p1 можна відновити p2.
# При використанні іншого ключа k2 ключі k1 і k2 не знищують один одного, тому простий спосіб відновлення вже не працює.
# Цей приклад не є атакою на правильно використаний сучасний потоковий шифр, а показує небезпеку повторного використання одного ключа.

