# reverse_toy_hash.py
from toy import toy_hash
import string
from itertools import product

def reverse_toy_hash(target_hash, max_len=5):
    charset = string.ascii_lowercase
    for length in range(1, max_len + 1):
        for attempt in product(charset, repeat=length):
            candidate = ''.join(attempt)
            if toy_hash(candidate) == target_hash:
                return candidate
    return None

# Example usage
target = toy_hash("abc")
print("Target hash:", target)
recovered = reverse_toy_hash(target)
print("Recovered input:", recovered)
