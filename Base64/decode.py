import base64

# def decode_base64(s):
#     return base64.b64decode(s)


#decode to hex   

s='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
y=bytes.fromhex(s)

#encode to base64
x=base64.b64encode(y)

#then decode that base64 into utf-8
# Convert to web-safe Base64 by replacing + with - and / with _
print(x.decode('utf-8').replace('+', '-').replace('/', '-'))


