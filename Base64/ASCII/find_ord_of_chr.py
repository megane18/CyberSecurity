
def ascii_find(s):

    result = []
    for char in range(len(s)):
        result.append(str(ord(s[char])))
    return result

# s=['M', 'e', 'g', 'a', 'n', 'e']
# print(' '.join(ascii_find(s)))
