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

