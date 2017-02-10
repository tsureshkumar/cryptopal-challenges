# https://cryptopals.com/sets/1/challenges/5
#
from base64 import b64encode, b64decode 
from binascii import hexlify, unhexlify

def xor(a,b):
    return bytes([x^y for (x,y) in zip(a,b)])

def enc(inpb,key):
    n = len(key)
    blks = [inpb[i:i+n] for i in range(0,len(inpb), n)]
    return b''.join([xor(x,key) for x in blks])

if __name__ == '__main__':

    inp = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    inpb = bytes(inp, 'utf-8')
    
    res = enc(inpb, b'ICE')
    print(hexlify(res) ==
          b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
    print(enc(res, b'ICE').decode("utf-8"))
#for i in inp.split("\n"):
#    print(i)
#    print(hexlify(enc(bytes(i, "utf-8"), b'ICE')).decode("utf-8"))
