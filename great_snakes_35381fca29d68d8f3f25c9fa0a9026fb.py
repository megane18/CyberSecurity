#!/usr/bin/env python3

import sys
# import this

# if sys.version_info.major == 2:
#     print("You are running Python 2, which is no longer supported. Please update to Python 3.")

# ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
# ord2=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# print("Here is your flag:")
# print("".join(chr(o ^ 0x32) for o in ord))
#for ord2
# print("".join(chr(o) for o in ord2))

sytm = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
print(bytes.fromhex(sytm))
