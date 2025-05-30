from itertools import product
import string
import time
from strong_hash import strong_toy_hash

def reverse_strong_hash(target_hash, salt="xZ1!", max_len=8):
    charset = string.ascii_letters + string.digits + "!@#$%&*"
    attempts = 0
    start = time.time()
    
    for length in range(1, max_len + 1):
        for guess in product(charset, repeat=length):
            word = ''.join(guess)
            if (any(c.islower() for c in word) and 
                any(c.isupper() for c in word) and 
                any(c.isdigit() for c in word) and 
                any(c in "!@#$%&*" for c in word)):
                attempts += 1
                if strong_toy_hash(word, salt) == target_hash:
                    duration = round(time.time() - start, 2)
                    return word, attempts, duration
    return None, attempts, round(time.time() - start, 2)

# Example usage:
if __name__ == "__main__":
    password = "Ab1#"
    salt = "xZ1!"
    target = strong_toy_hash(password, salt)
    print("Target hash:", target)

    found, tries, time_taken = reverse_strong_hash(target, salt, max_len=6)
    if found:
        print(f"Recovered password: {found}")
        print(f"Tries: {tries}")
        print(f"Time taken: {time_taken}s")
    else:
        print("Failed to reverse within given constraints.")
