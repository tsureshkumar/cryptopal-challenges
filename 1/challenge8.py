# https://cryptopals.com/sets/1/challenges/8

from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
import itertools

def main():
    plain = open('8.txt').read()
    for line in plain.split('\n'):
        line = unhexlify(line)
        blks = [line[i:i+16] for i in range(0,len(line), 16)]
        sb = sorted(blks)
        if any([sb[i] == sb[i-1] for i in range(1,len(sb))]):
            print("This line is encrypted with CBC:")
            print(hexlify(line))
        #cmbs = itertools.combinations(blks, 2)
        #print(any([p[0] == p[1] for p in cmbs]))

if __name__ == '__main__':
    main()
