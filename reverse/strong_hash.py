import string

def strong_toy_hash(msg, salt="xZ1!"):
    # Stretching: repeat the hashing 1000 times
    total = sum((ord(ch) + ord(salt[i % len(salt)])) ^ (i + 17) for i, ch in enumerate(msg))
    for _ in range(1000):
        total = ((total << 3) ^ (total >> 2)) + 1337
        total = total % 10**8  # limit size
    return hex(total)


# print(strong_toy_hash(msg='aA2!'))