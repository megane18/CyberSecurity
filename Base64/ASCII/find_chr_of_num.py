import base64
def find_chr_of_ord(s):

    result = []
    for item in s:
        if item not in result:
            result.append(chr(item))
    return result


# s=[77,101,103,97,110,101]
# print(''.join(find_chr_of_ord(s)))


# convert the following int to message
s=11515195063862318899931685488813747395775516287289682636499965282714637259206269
from Crypto.Util.number import long_to_bytes
message = long_to_bytes(s)
print(message)



















































































































