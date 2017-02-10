# https://cryptopals.com/sets/1/challenges/6

from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify
import itertools
from functional import compose, partial

import challenge1
import challenge4
import challenge5

def hamming(s1,s2):
    return sum([bin(s1[i]^s2[i]).count('1') for i in range(0,len(s1))])



# hints from https://github.com/akalin/cryptopals-python3/blob/master/challenge6.py
# normalized score for guessed keysize
def norm(ks):
    #blks = [content[i:i+ks] for i in range(0,len(content), ks)][0:2]
    #return hamming(blks[0], blks[1])/ks
    blks = [content[i:i+ks] for i in range(0,len(content), ks)][0:4]
    scores = list(map(lambda x:hamming(x[0],x[1])/ks, itertools.combinations(blks,2)))[0:6]
    return sum(scores)/len(scores)

def breakKey(content, ks):
    blks = [content[i:i+ks] for i in range(0,len(content), ks)]
    tblks = list(itertools.zip_longest(*blks, fillvalue=0)) # transposed blocks
    key = bytes(list(map(compose(lambda x:x[0], challenge4.findkey), tblks)))
    return key

if __name__ == '__main__':
    assert(hamming(b"this is a test", b"wokka wokka!!!") == 37)
    content = b64decode(open("6.txt", "rb").read())
    ks = min(range(2,41), key=norm) #guess the key size
    key = breakKey(content, ks)
    print("key :", key)
    print(challenge5.enc(content, key).decode("utf-8"))
