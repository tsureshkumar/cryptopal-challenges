# https://cryptopals.com/sets/1/challenges/4

from base64 import b64encode, b64decode 
from binascii import hexlify, unhexlify

# From http://www.data-compression.com/english.html
freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}

def score(x):
    letters = [chr(i).lower() for i in x]
    s = list(map(lambda y: freqs.get(y, 0), letters))
    return sum(s)

def findkey(inpb):
    # list of tuple (key, score)
    ks = [(k, score(bytes(x^k for x in inpb))) for k in range(1,256)]
    return max(ks, key=lambda x: x[1])

if __name__ == '__main__':
    eng_like_line = ""
    m=0
    k=0
    with open("4.txt") as f:
        for x in f:
            if ord(x[-1]) == 10: # newline
                x = x[:-1]
                (k1, m1) = findkey(unhexlify(x))
                if (m < m1):
                    m = m1
                    k = k1
                    eng_like_line = x
    print(bytes([t^k for t in unhexlify(eng_like_line)]))
