import base64
#hex to raw "hex decoding"
raw = base64.b16decode("string", True) #accept lowercase?
print(raw)

#raw to base64
b64 = base64.b64encode(raw)
print(b64)

#--------------
frombase = 16

number = int(number, frombase)
bin(newnumber)
hex(newnumber)
oct(newnumber)