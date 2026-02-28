# import sys
# chars = ""
# from fileinput import input
# for line in input():
#   chars += line

# lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
# lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

# out = ""

# prev = 0
# for char in chars:
#   cur = lookup1.index(char)
#   out += lookup2[(cur - prev) % 40]
#   prev = cur

# sys.stdout.write(out)

import sys
from fileinput import input

# Read ciphertext from stdin (file or pipe)
chars = ""
for line in input():
    chars += line.strip("\n")

# Correct 40-character alphabet for this picoCTF challenge
lookup1 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

# Sanity check
if len(lookup1) != 40:
    print("lookup1 length error:", len(lookup1))
    sys.exit(1)

# Decode
out = ""
prev = 0

for ch in chars:
    if ch not in lookup1:
        print("Invalid character found:", ch)
        sys.exit(1)

    cur = lookup1.index(ch)
    out += lookup2[(cur - prev) % 40]
    prev = cur

# Output plaintext
sys.stdout.write(out)

