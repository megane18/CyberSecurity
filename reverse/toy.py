# toy_hash.py
def toy_hash(msg):
    total = 0
    for i, ch in enumerate(msg):
        total += (ord(ch) * (i + 1))  # Add character value multiplied by position
    return hex(total % 100000)  # Return 5-digit hex


print(toy_hash("abc"))  # Let's say: 0x0309c
