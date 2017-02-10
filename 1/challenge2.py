from base64 import b64encode, b64decode 
from binascii import hexlify, unhexlify

def hex_to_base64(str):
    return b64encode(unhexlify(str))

def base64_to_hex(str):
    return hexlify(b64decode(str))

inp1 = b"1c0111001f010100061a024b53535009181c"
inp2 = b"686974207468652062756c6c277320657965"
outp = b"746865206b696420646f6e277420706c6179"


if __name__ == '__main__':
    res = hexlify(bytearray(x^y for x,y in zip(unhexlify(inp1), unhexlify(inp2))))
    assert(res == outp)
    print(res)

