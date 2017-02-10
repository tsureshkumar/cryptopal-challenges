import base64 
import binascii

def hex_to_base64(str):
    return base64.b64encode(binascii.unhexlify(str))

def base64_to_hex(str):
    return binascii.hexlify(base64.b64decode(str))

assert(
        hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
        == 
 b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

